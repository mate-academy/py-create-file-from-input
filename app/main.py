def main() -> None:
    file_name = str(input("Enter name of the file: ") + ".txt")
    text = ""
    while True:
        new_line = input("Enter new line of content: ")
        if new_line != "stop":
            text += new_line + "\n"
        else:
            break
    with open(file_name, "w") as file:
        file.write(text)


if __name__ == "__main__":
    main()
