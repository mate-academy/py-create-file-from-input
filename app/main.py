def main() -> None:
    """
    Main function to create a text file based on user input.
    """
    file_name = input("Enter name of the file: ")
    file_name = f"{file_name}.txt"
    content_lines = []

    while True:
        # Ask for a new line of content
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    # Write content to the file
    with open(file_name, "w") as file:
        file.write("\n".join(content_lines))
    print(
        f'File "{file_name}" created successfully.'
    )


if __name__ == "__main__":
    main()
