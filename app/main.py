def main() -> None:
    name = input("Enter name of the file: ")
    new_line = ""
    new_text = ""

    while new_text != "stop":
        new_text = input("Enter new line of content: ")
        if new_text != "stop":
            new_line += new_text + "\n"

    with open(f"{name}.txt", "w") as content:
        content.write(new_line)


if __name__ == "__main__":
    main()
