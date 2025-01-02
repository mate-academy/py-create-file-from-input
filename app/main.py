def main():
    # Ask user for file name
    file_name = input("Enter name of the file: ")

    # Add .txt extension
    file_name = f"{file_name}.txt"

    # Initialize an empty list for content
    content = []

    # Prompt user to enter lines of content until 'stop' is entered
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == 'stop':
            break
        content.append(line)

    # Write content to the file
    with open(file_name, 'w') as file:
        for line in content:
            file.write(line + '\n')

    print(f"File '{file_name}' has been created successfully.")


if __name__ == "__main__":
    main()
