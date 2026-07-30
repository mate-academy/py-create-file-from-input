def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    new_line = None
    with open(file_name, "w") as file:
        while new_line != "stop":
            new_line = input("Enter new line of content: ")
            if new_line != "stop":
                file.write(new_line + "\n")


if __name__ == "__main__":
    main()
