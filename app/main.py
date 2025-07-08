def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    result_data = []
    new_line = ""

    while new_line != "stop":
        if new_line:
            result_data.append(new_line)
        new_line = input("Enter new line of content: ")

    with open(file_name, "w") as file:
        for elem in result_data:
            file.write(f"{elem}\n")


if __name__ == "__main__":
    main()
