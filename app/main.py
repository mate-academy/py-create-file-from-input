def main() -> None:
    file_name = input("Enter name of the file: ")
    while not file_name:
        file_name = input("Enter correct name of the file: ")

    rows_content = []
    row_content = input("Enter new line of content: ")
    while row_content != "stop":
        rows_content.append(row_content + "\n")
        row_content = input("Enter new line of content: ")

    with open(file_name + ".txt", "w") as f:
        for row in rows_content:
            f.write(row)


if __name__ == "__main__":
    main()
