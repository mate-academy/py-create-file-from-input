def main() -> None:
    # write your code here
    file_name = input("Enter name of the file: ") + ".txt"

    content_lines = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        content_lines.append(new_line)

    with open(file_name, "w") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f"File '{file_name}' has been created with the provided content.")


if __name__ == "__main__":
    main()
