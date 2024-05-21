def main() -> None:
    file_name = input("Enter name of the file: ")

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    file_name += ".txt"

    with open(file_name, "w") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f"File '{file_name}' has been created successfully.")


if __name__ == "__main__":
    main()
