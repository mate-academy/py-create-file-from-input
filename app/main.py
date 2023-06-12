def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []

    while True:
        input_line = input("Enter new line of content: ")
        if input_line == "stop":
            break
        content.append(input_line)

    with open(file_name + ".txt", "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
