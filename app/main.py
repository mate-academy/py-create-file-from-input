def main() -> None:
    file_name = input("Enter name of the file: ")
    result = ""
    input_line = input("Enter new line of content: ")
    while input_line != "stop":
        result += input_line + "\n"
        input_line = input("Enter new line of content: ")

    with open(file_name + ".txt", "w") as file:
        file.write(result)


if __name__ == "__main__":
    main()
