## Project Description

This project is to perform document extraction from PDF files using optical character recognition (OCR) with Pytesseract.

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

activate environtment
```bash
  .\.venv\Scripts\activate
```

if linux
```bash
    source .venv/bin/activate (linux)
```

after activate enviroment, Install packages

```bash
  pip install -r requirements.txt
```

Run project

```bash
    python .\main.py .\OCBC.pdf
```