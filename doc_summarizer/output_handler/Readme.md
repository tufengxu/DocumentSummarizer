# How to use OutputHandler

## Required packages
1. wkhtmltopdf
https://wkhtmltopdf.org/downloads.html
2. pdfkit

## Usage
```python
from doc_summarizer.output_handler import OutputHandler
out_hd = OutputHandler(Summary)
out_hd.GeneratePdf()
```

## Input format
string


