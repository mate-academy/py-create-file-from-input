def main() -> None:
    """
    Enter name of the file: name1
    Enter new line of content: This is the first line of content
    Enter new line of content: This is the second
    Enter new line of content: stop
    """
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    with open(file_name, "w") as file:
        while True:
            line = input("Enter new line of content: ")

            if line == "stop":
                break

            file.write(line + "\n")


if __name__ == "__main__":
    main()
