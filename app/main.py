def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    content = []
    while True:
        content_row = input("Enter new line of content: ")
        if content_row == "stop":
            break
        content.append(content_row + "\n")
    with open(filename, "w") as file:
        for row in content:
            file.write(row)


if __name__ == "__main__":
    main()
