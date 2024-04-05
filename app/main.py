def main() -> None:
    file_name = input("Enter name of the file: ")
    input_content = []
    value = ""
    while value != "stop":
        if value:
            input_content.append(value)
        value = input("Enter new line of content: ")

    with open(file_name + ".txt", "w") as file:
        for item in input_content:
            file.write(item + "\n")


if __name__ == "__main__":
    main()
