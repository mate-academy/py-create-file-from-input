def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    text = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        text.append(line)

    with open(file_name, "w") as file:
        for line in text:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
