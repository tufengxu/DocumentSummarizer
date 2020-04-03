from doc_summarizer.input_handler import InputHandler

in_hd = InputHandler()


def test_input_txt():
    in_hd.clear()
    result = in_hd.txt("input_handler/example.txt")
    assert result[0] == "This is line 0."
    assert result[9] == "(sry i lied cuz i wanna add 10th line"


def test_input_pdf():
    in_hd.clear()
    result = in_hd.pdf("input_handler/example.pdf")
    assert result[0] == "This is line 0. "
