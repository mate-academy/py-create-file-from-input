def main() -> None:
    """Main function to create a file with user-provided name and content."""
    # Get the file name from the user
    file_name = input("Enter name of the file: ")

    # Initialize an empty list to store content lines
    content_lines = []

    print("Enter new lines of content (type 'stop' to finish):")

    # While loop to collect content lines
    while True:
        line = input("Enter new line of content: ")

        # Check if user wants to stop
        if line.lower() == "stop":
            break

        # Add the line to our content list
        content_lines.append(line)

    # Create the full file name with .txt extension
    full_file_name = f"{file_name}.txt"

    # Write content to the file
    try:
        with open(full_file_name, "w", encoding="utf-8") as file:
            for content_line in content_lines:
                file.write(content_line + "\n")

        print(f"\nFile '{full_file_name}' has been created successfully!")

        # Display file content preview
        print("File content:")
        for content_line in content_lines:
            print(content_line)

    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


if __name__ == "__main__":
    main()
