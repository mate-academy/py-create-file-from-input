def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content_lines = []

    while True:
        user_input = input("Enter new line of content: ")
        if user_input.lower() == "stop":
            break
        content_lines.append(user_input)

    with open(file_name, "w") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f"File {file_name} created successfully with the provided content.")


if __name__ == "__main__":
    main()
