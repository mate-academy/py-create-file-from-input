def main() -> None:
    # Get file name from user
    filename = input("Enter name of the file: ")

    # Add .txt extension if not present
    if not filename.endswith(".txt"):
        filename += ".txt"

    # Initialize empty list to store content lines
    content = []

    # Loop to get content from user
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    # Write content to file
    try:
        with open(filename, "w") as file:
            for line in content:
                file.write(line + "\n")
        print(f"\nFile '{filename}' has been created successfully!")

        # Display file content
        print("\nFile content:")
        for line in content:
            print(line)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
