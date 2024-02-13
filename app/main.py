def main() -> None:
    text = ""

    while True:
        file_name = input("Enter name of the file: ")
        if file_name != "":
            break

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        text += line + "\n"

    with open(file_name + ".txt", "w") as file:
        file.write(text)


if __name__ == "__main__":
    main()
