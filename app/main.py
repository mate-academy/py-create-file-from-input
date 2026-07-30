def main() -> None:
    file_name = input("Enter name of the file: ")
    correct_file_name = file_name + ".txt"

    text = ""
    line = ""

    while "stop" not in line:
        line = input("Enter new line of content: ")
        if line != "stop":
            text += line + "\n"

    with open(correct_file_name, "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
