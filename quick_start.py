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

    target_path = "out/output.pdf"
    smrzr = DocSummarizer()
    # fixme : output failed
    # try this file: misc/example.txt
    if suffix == ".txt":
        smrzr.txt(filepath, target_path)
    else:
        smrzr.pdf(filepath, target_path)


if __name__ == '__main__':
    run()
