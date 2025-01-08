def main() -> None:
    # Ask the user to enter the name of the file
    file_name = input("Enter name of the file: ")

    # Append .txt extension to the file name
    file_name = f"{file_name}.txt"

    # Initialize an empty list to store content
    content = []

    while True:
        # Ask the user to enter the next line of content
        line = input("Enter new line of content: ")

        # Check if the user entered 'stop'
        if line.lower() == "stop":
            break

        # Append the line to the content list
        content.append(line)

    # Write the content to the file
    with open(file_name, "w") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
