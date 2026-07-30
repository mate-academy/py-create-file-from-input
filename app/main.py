def main() -> None:
    file_name = input("Enter name of the file: ")
    new_file = f"{file_name}.txt"

    content = []

    while True:
        next_line = input("Enter new line of content: ")
        if next_line == "stop":
            break
        content.append(next_line)

    with open(new_file, "a") as file:
        for line in content:
            file.write(line + "\n")

    print(f'File "{new_file}" has been created.')


if __name__ == "__main__":
    main()
