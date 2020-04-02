from doc_summarizer.input_handler import read_pdf
from doc_summarizer.input_handler.read_txt import read_txt


class InputHandler(object):
    def __init__(self):
        self.result = list()

    def pdf(self, filepath):
        with open(filepath, "rb") as my_pdf:
            self.result = read_pdf(my_pdf)
        return self.result

    def txt(self, filepath):
        with open(filepath, "r") as my_txt:
            self.result = read_txt(my_txt)
        return self.result
