def main() -> None:
    """
    Main function to create a text file based on user input.
    """
    # Ask for the file name
    file_name = input("Enter name of the file: ")
    file_name = f"{file_name}.txt"  # Add .txt extension

    # Initialize a list to store content lines
    content_lines = []

    while True:
        # Ask for a new line of content
        line = input("Enter new line of content: ")
        if line.lower() == "stop":  # Stop if the user enters "stop"
            break
        content_lines.append(line)  # Add the line to the list

    # Write content to the file
    with open(file_name, "w") as file:
        file.write("\n".join(content_lines))  # Write all lines, joined by newlines

    # Print success message
    print(f'File "{file_name}" created successfully.')


if __name__ == "__main__":
    main()
