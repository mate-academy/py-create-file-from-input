def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = []

    while True:
        input_line = input("Enter new line of content: ")
        if input_line == "stop":
            break
        content.append(input_line)

    with open(file_name, "w") as file:
        file.write("\n".join(content))

    print(f"File '{file_name}' created!")


if __name__ == "__main__":
    main()
