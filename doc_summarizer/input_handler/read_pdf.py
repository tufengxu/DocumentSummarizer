from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import process_pdf


# It is unavoidable that there will be some empty lines between different paragraph styles.
def read_pdf(pdf):
    # resource manager
    rsrc_mgr = PDFResourceManager()
    ret_str = StringIO()
    laparams = LAParams()
    # device
    device = TextConverter(rsrc_mgr, ret_str, laparams=laparams)
    process_pdf(rsrc_mgr, device, pdf)
    device.close()
    content = ret_str.getvalue()
    ret_str.close()
    # get all lines
    lines = str(content).split("\n")
    return lines


if __name__ == '__main__':
    with open("example.pdf", "rb") as my_pdf:
        stored = read_pdf(my_pdf)
        idx = 0
        for item in stored:
            print("Line ID: ", idx, "  Line: ", item)
            idx += 1
