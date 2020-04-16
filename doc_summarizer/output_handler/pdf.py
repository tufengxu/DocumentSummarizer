#!/usr/bin/python
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def GeneratePdf(Summary):
    
    c = canvas.Canvas("Summary.pdf")
    c.setFont("Courier",35) 
    # print(c.getAvailableFonts())
    title="Summary: "
    c.drawString(50,750,title)
    c.setFont("Times-Roman",16)
    sentences = Summary.split("\n")
    i = 0
    for sentence in sentences:
      c.drawString(70,700-25*i,sentence)
      i = i + 1
    c.showPage()
    c.save()

if __name__ == '__main__':
  Summary = "This is a Summary\nxixixixi\nnext line\n"
  print(Summary)
  GeneratePdf(Summary);

