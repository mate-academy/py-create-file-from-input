def main() -> None:
    file_name: str = input("Enter name of the file: ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    user_generated_lines: list = []

    while True:
        line: str = input("Enter new line of content: ")
        if line == "stop":
            break
        user_generated_lines.append(line)

    with open(file_name, "w") as file:
        file.writelines(line + "\n" for line in user_generated_lines)


if __name__ == "__main__":
    main()
