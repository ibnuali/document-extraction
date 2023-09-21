from PIL import Image
import pandas as pd
import pytesseract
import fitz
import sys
import re

pdf_path = sys.argv[1]
# change path tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Ibnu_A016\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
split_results = []
tgl_trans_dates = []
tgl_valuta_dates = []
keterangan = []

def getTextFromPDF(pdf):
    ocr_results = []
    doc = fitz.open(pdf)
    for page in doc:
        # crop image of table
        left = 0  
        top = 100
        mediabox = page.mediabox 

        right = mediabox[2] 
        bottom = mediabox[3] - 170

        zoom_x = 2.4 
        zoom_y = 2.4 

        mat = fitz.Matrix(zoom_x, zoom_y)
        pix = page.get_pixmap(matrix=mat, clip=(left, top, right, bottom))
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        text = pytesseract.image_to_string(img, lang='eng')
        
        ocr_results.append(text)
    
    return ocr_results
    

results = getTextFromPDF(pdf_path)

for ocr_result in results:
    clean_text = ocr_result.replace("]", "").replace("}", "").replace("|", "")
    split_results.extend(clean_text.split('\n\n'))

date_pattern = r'\d{2}/\d{2}/\d{2}'
pattern_unstructure_date = r'\)?\s*\d{2}/\d{2}/\d{2}\)?\s*'

for line in split_results:
    if ". DEBET KREDIT SALDO ~" in line or "DEBET KREDIT SALDO" in line:
        continue
    matches = re.findall(date_pattern, line)
    if len(matches) == 2:
        tgl_trans_dates.append(matches[0])
        tgl_valuta_dates.append(matches[1])
        keterangan_text = line.split(matches[1], 1)[1].strip()
        cleaned_column_keterangan = re.sub(pattern_unstructure_date, '', keterangan_text)
        keterangan.append(cleaned_column_keterangan)
    else:
        tgl_trans_dates.append(None)
        tgl_valuta_dates.append(None)
        keterangan.append(line)


df = pd.DataFrame({
    'TGL_TRANS': tgl_trans_dates,
    'TGL_VALUTA': tgl_valuta_dates,
    'KETERANGAN': keterangan,
})

excel_writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
df.to_excel(excel_writer, index=False)
excel_writer._save()