def main() -> None:
    name = input("Enter name of the file: ")
    name_file = name + ".txt"
    line_text = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        line_text.append(line)
    content = "\n".join(line_text)
    with open(name_file, "a") as file:
        file.write(content)


if __name__ == "__main__":
    main()
