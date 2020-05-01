<!--

General thought:
    1. convert a pdf file into a text file
    2. summarize the text file
    3. convert the summarized text into a pdf feedback

-->


# Document Summarizer


## Project Description
### Project Function
Input:  the document to be summarized, should be a TXT or PDF file.

Output: summarized document, could be a PDF file.

Architecture: 
<img src=".misc/Architecture.png">

### User Stories
- I, an editor, want to get key points of a document instead of reading the whole file. :expressionless:


## Install
### OS X
```sh
$ brew cask install wkhtmltopdf
```

### Otherwise
Please go to the [wkhtmltopdf download page](https://wkhtmltopdf.org/downloads.html)


## Usage
### Quick Start
As an independent program running in the console:

```sh
# You can simply try this file: misc/example.txt

$ python quick_start.py
Where is your file?
Path: misc/example.txt
Loading pages (1/6)
Counting pages (2/6)                                               
Resolving links (4/6)                                                       
Loading headers and footers (5/6)                                           
Printing pages (6/6)
Done
```

Now there is a PDF file called `output.pdf` in the current directory.

### API
As a module called by other program:

```python
from doc_summarizer import DocSummarizer

smrzr = DocSummarizer()

# note that the target is file name, not the path!! 
target = "output.pdf" 
filepath_txt = "/path/to/input.txt"
filepath_pdf = "/path/to/input.pdf"

# dealing with .txt files
smrzr.txt(filepath_txt, target)
# dealing with .pdf files
smrzr.pdf(filepath_pdf, target)
```


## Contributors
- [@E1visz](https://github.com/E1visz)
- [@JWangNov](https://github.com/JWangNov)
- [@tufengxu](https://github.com/tufengxu)

## Reference
TextTeaser: https://github.com/IndigoResearch/textteaser   
TextTeaser Chinese: https://github.com/nanpian/textteaser-chinese   
