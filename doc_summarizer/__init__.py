from doc_summarizer.input_handler import InputHandler
from doc_summarizer.output_handler import OutputHandler
from doc_summarizer.textteaser import TextTeaser


class DocSummarizer:
    def __init__(self):
        self.in_hd = InputHandler()
        self.teaser = TextTeaser()
        self.input_lines = list()

    def pdf(self, filepath):
        # store file content, line by line, in a list
        self.input_lines = self.in_hd.pdf(filepath)
        # use input[0] as the title
        input_title = self.input_lines[0]
        paragraph = self.teaser.summarize(input_title, self.input_lines)
        # generate output
        out_hd = OutputHandler(paragraph)
        out_hd.GeneratePdf()

    def txt(self, filepath):
        self.input_lines = self.in_hd.txt(filepath)
        input_title = self.input_lines[0]
        paragraph = self.teaser.summarize(input_title, self.input_lines)
        out_hd = OutputHandler(paragraph)
        out_hd.GeneratePdf()
