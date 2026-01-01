def main() -> None:
    user_input = input("Enter name of the file: ")
    file_name = f"{user_input}.txt"
    file_content: list[str] = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        file_content.append(line)

    input_file = open(file_name, "w")
    for line in file_content:
        input_file.write(line + "\n")
    input_file.close()


if __name__ == "__main__":
    main()
