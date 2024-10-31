def main() -> None:
    """Prompts user for a file name and content, then creates the file."""
    file_name = input("Enter name of the file: ").strip() + ".txt"

    content = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(file_name, "w") as file:
        file.write("\n".join(content))

    print(f'File "{file_name}" has been created with the following content: ')
    for line in content:
        print(line)


if __name__ == "__main__":
    main()
