def main() -> None:
    text = []
    file_name = input("Enter name of the file: ") + ".txt"
    row = input("Enter new line of content: ")
    while row != "stop":
        text.append(row)
        row = input("Enter new line of content: ")
    with open(file_name, "w") as file:
        for row in text:
            print(row, file=file)


if __name__ == "__main__":
    main()
