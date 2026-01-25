def main() -> None:
    # Ask the user for the file name
    file_name = input("Enter name of the file: ")

    # Append '.txt' extension to the file name
    file_name_with_extension = file_name + ".txt"

    # Initialize an empty list to hold the file content
    content_lines = []

    # Loop to collect lines of content from the user
    while True:
        line = input("Enter new line of content: ")

        # Stop collecting lines if the user enters 'stop'
        if line.lower() == "stop":
            break

        # Add the line to the list
        content_lines.append(line)

    # Write the collected content to the file
    with open(file_name_with_extension, "w") as file:
        for line in content_lines:
            file.write(line + "\n")

    # Inform the user that the file has been created
    print(f'# File name: "{file_name_with_extension}"')
    print("# File content:")
    for line in content_lines:
        print(f"# {line}")


if __name__ == "__main__":
    main()
