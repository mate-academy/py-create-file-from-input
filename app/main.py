def create_file() -> None:
    # Ask user for the file name
    file_name = input("Enter name of the file: ") + ".txt"

    # Open the file in write mode
    with open(file_name, "w") as file:
        while True:
            # Ask for a new line of content
            line = input("Enter new line of content: ")
            if line.lower() == "stop":
                break
            # Write the line to the file
            file.write(line + "\n")

    print(f"File '{file_name}' has been created with the provided content.")


def main() -> None:
    create_file()


if __name__ == "__main__":
    main()
