def main() -> None:
    """
    This function prompts the user to enter a file name and allows them
    to write lines of content to the file until they type "stop".
    """
    file_name = input("Enter name of the file: ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    with open(file_name, "w") as file:
        while True:
            line = input("Enter new line of content: ")
            if line.lower() == "stop":
                break
            file.write(line + "\n")


if __name__ == "__main__":
    main()
