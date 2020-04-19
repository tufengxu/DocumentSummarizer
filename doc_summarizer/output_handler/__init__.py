from doc_summarizer.output_handler.pdf import GeneratePdf


class OutputHandler(object):
    def __init__(self, Summary, Filename):
      self.sum = Summary
      self.filename = Filename
    
    def GeneratePdf(self):
        GeneratePdf(self.sum, self.filename)
