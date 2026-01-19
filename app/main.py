def main() -> None:
    # Ask the user for the file name
    file_name = input("Enter name of the file: ")

    # Ensure the file has a .txt extension
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    # Prepare an empty list to store content lines
    content_lines = []

    # Loop to gather content until user enters 'stop'
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    # Write the collected content to the file
    with open(file_name, "w") as file:
        for line in content_lines:
            file.write(line + "\n")

    # Confirm file creation
    print(f'File "{file_name}" has been created with the following content:')
    for line in content_lines:
        print(line)


if __name__ == "__main__":
    main()
