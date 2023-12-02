def main():
    text = ""
    name = input("Enter name of the file: ")
    line = input("Enter new line of content: ")
    while line != "stop":
        text += line + "\n"
        line = input("Enter new line of content: ")
    text = text[:-1:]
    with open(name + ".txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
