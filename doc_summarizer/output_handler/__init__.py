from doc_summarizer.output_handler.pdf import GeneratePdf


class OutputHandler(object):
    def __init__(self, Summary):
      self.sum = Summary
    
    def GeneratePdf(self):
        GeneratePdf(self.sum)