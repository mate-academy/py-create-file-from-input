def main() -> None:
    # Ask the user for the file name
    file_name = input("Enter name of the file: ") + ".txt"

    # Initialize an empty list to store the content
    content = []

    # Continuously ask for input until 'stop' is entered
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    # Writing the content to the file
    with open(file_name, "w") as file:
        for line in content:
            file.write(line + "\n")

    print(f'File "{file_name}" has been created successfully.')


if __name__ == "__main__":
    main()
