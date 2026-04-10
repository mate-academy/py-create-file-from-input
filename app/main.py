def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    while True:
        input_line = input("Enter new line of content: ")
        if input_line == "stop":
            break
        content.append(f"{input_line}\n")
    with open(f"{file_name}.txt", "w") as file:
        file.writelines(content)


if __name__ == "__main__":
    main()
