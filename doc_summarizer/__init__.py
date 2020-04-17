from doc_summarizer.input_handler import InputHandler
from doc_summarizer.output_handler import OutputHandler
from doc_summarizer.textteaser import TextTeaser


class DocSummarizer:
    def __init__(self):
        self.in_hd = InputHandler()
        self.teaser = TextTeaser()
        self.input_lines_list = list()
        self.text_str = str()

    def pdf(self, filepath):
        # store file content, line by line, in a list
        self.input_lines_list = self.in_hd.pdf(filepath)
        # use input[0] as the title
        input_title = self.input_lines_list[0]
        self.get_text_str()
        paragraph = self.teaser.summarize(input_title, self.text_str)
        # generate output
        out_hd = OutputHandler(paragraph)
        out_hd.GeneratePdf()

    def txt(self, filepath):
        self.input_lines_list = self.in_hd.txt(filepath)
        input_title = self.input_lines_list[0]
        self.get_text_str()
        paragraph = self.teaser.summarize(input_title, self.text_str)
        out_hd = OutputHandler(paragraph)
        out_hd.GeneratePdf()

    def get_text_str(self):
        for one_line in self.input_lines_list:
            if one_line == "":
                continue
            self.text_str += one_line
