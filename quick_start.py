import os

from doc_summarizer import DocSummarizer


def run():
    print("Where is your file?")
    filepath = input("Path: ")
    if filepath.find(".") == -1:
        raise Exception("Nein! Nein! Nein! Nein! Nein!\nCannot find suffix!!")

    suffix = os.path.splitext(filepath)[-1]

    if suffix != ".txt" and suffix != ".pdf":
        raise Exception("Nein! Nein! Nein! Nein! Nein!\nNot a .pdf or .txt file!!")

    target = "output.pdf"
    smrzr = DocSummarizer()
    # try this file: misc/example.txt
    if suffix == ".txt":
        smrzr.txt(filepath, target)
    else:
        smrzr.pdf(filepath, target)


if __name__ == '__main__':
    run()
