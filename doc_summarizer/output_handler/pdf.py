import pdfkit


def GeneratePdf(summary, filename):
    pdfkit.from_string(summary, filename)


if __name__ == '__main__':
    Summary = "This is a Summary\nxixixixi\nnext line\n"
    print(Summary)
    GeneratePdf(Summary, "unittest.pdf");
