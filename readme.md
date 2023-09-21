## Project Description

This project is to perform document extraction from PDF files using optical character recognition (OCR) with Pytesseract.

## Prerequisites
Before you get started, make sure you have the following prerequisites in place:

Python: Ensure you have Python 3.x installed on your system. I used Python version 3.10.11
Tesseract-OCR: Install Tesseract-OCR on your system. You can download it from the official website.
[Download Here](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe)

if you are using linux
```bash
  sudo apt install tesseract-ocr
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/ibnuali/document-extraction
```

Go to the project directory

```bash
  cd document-extraction
```

Create virtual environtment
```bash
  python -m venv .venv
```

activate environtment (windows)
```bash
  .\.venv\Scripts\activate
```

if linux you are using linux
```bash
  source .venv/bin/activate
```

after activate enviroment, Install packages

```bash
  pip install -r requirements.txt
```

Run project

```bash
    python .\main.py .\OCBC.pdf
```