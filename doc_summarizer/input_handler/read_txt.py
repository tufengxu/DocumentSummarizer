def read_txt(txt):
    lines = list()
    for line in txt:
        lines.append(line.strip("\n"))
    return lines


if __name__ == '__main__':
    with open("example.txt", "r") as my_txt:
        stored = read_txt(my_txt)
        idx = 0
        for item in stored:
            print("Line ID: ", idx, "  Line: ", item)
            idx += 1
