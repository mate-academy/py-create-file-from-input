def main() -> None:
    file_name = input("Enter name of the file: ")
    new_line = ""
    text = ""
    while new_line != "stop":
        if new_line:
            text += new_line + "\n"
        new_line = input("Enter new line of content: ")
    with open(file_name + ".txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
