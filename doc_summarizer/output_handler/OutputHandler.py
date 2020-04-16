import pdfkit


def summary_to_pdf(filename, summary):
    pdfkit.from_string(summary, filename)
