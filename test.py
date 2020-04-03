#!/usr/bin/python
# -*- coding: utf-8 -*-

from doc_summarizer.input_handler import InputHandler
from textteaser import TextTeaser


in_hd = InputHandler()
result_pdf = in_hd.pdf("/path/to/file.pdf")
result_txt = in_hd.txt("/path/to/file.txt")

title = result_pdf[0]
text = ""
for ii in range(1, len(result_pdf)):
       text += result_pdf[ii]

tt = TextTeaser()
sentences = tt.summarize(title, text)

summary = ""
for sentence in sentences:
    summary += sentence
print(summary)
