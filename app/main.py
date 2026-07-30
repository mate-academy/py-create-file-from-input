def create_file() -> None:
    # Get the file name from the user
    file_name = input("Enter name of the file: ") + ".txt"

    # Initialize an empty list to hold content lines
    content_lines = []

    # Loop to gather lines of content until 'stop' is entered
    while True:
        line = input("Enter new line of content: ")

        if line.lower() == "stop":
            break

        content_lines.append(line)

        # Write content to the file
    with open(file_name, "w") as file:
        file.write("\n".join(content_lines))

    print(f"File '{file_name}' created with the provided content.")


def main() -> None:
    create_file()


if __name__ == "__main__":
    main()
