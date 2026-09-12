def read_file(filename=""):
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")
