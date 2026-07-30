def main():
    name = input("Enter name of the file: ")
    text = input("Enter new line of content: ")
    text_by_line = []
    while text != "stop":
        text_by_line.append(text)
        text = input("Enter new line of content: ")
    with open(name + ".txt", "w") as file:
        for line in text_by_line:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
