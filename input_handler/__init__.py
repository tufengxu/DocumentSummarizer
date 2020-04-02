from input_handler.read_pdf import read_pdf


class InputHandler(object):
    def __init__(self):
        self.result = list()

    def pdf(self, filepath):
        with open(filepath, "rb") as my_pdf:
            self.result = read_pdf(my_pdf)
        return self.result
