How to use output_handler


## Usage   

1. Install pdfkit
```python
pip install pdfkit  (or pip3 for python3)   
```
2. Install wkhtmltopdf   
MacOS: 
```
brew cask install wkhtmltopdf
```   
Ubuntu:   
```
sudo apt-get install wkhtmltopdf   
``` 



3. how to use   

```python
from doc_summarizer.output_handler import OutputHandler
out_hd = OutputHandler(Summary, filepath)
//filepath == "./test.pdf"
out_hd.GeneratePdf()
```

reference:   
https://github.com/JazzCore/python-pdfkit
