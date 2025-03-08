def main() -> None:
    # Ask the user to enter the file name
    file_name: str = input("Enter name of the file: ")

    # Initialize an empty list to store the content
    content: list[str] = []

    # Loop to get content lines from the user
    while True:
        line: str = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    # Create the file with the provided name and .txt extension
    with open(f"{file_name}.txt", "w") as file:
        for line in content:
            file.write(line + "\n")

    print(f"File '{file_name}.txt' has been created successfully.")


if __name__ == "__main__":
    main()