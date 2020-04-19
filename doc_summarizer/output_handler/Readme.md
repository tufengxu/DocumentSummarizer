How to use output_handler


## Usage   

1. Install pdfkit
```python
pip install pdfkit  (or pip3 for python3)   
```
2. Install wkhtmltopdf   
MacOS: 
```
brew install caskroom/cask/wkhtmltopdf  
```   
Ubuntu:   
```
brew install caskroom/cask/wkhtmltopdf   
``` 



3. 

```python
from doc_summarizer.output_handler import OutputHandler
out_hd = OutputHandler(Summary, filepath)
//filepath == "./test.pdf"
out_hd.GeneratePdf()
```

reference:   
https://github.com/JazzCore/python-pdfkit
