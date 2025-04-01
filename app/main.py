def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(file_name + ".txt", "w") as file:
        new_line = input("Enter new line of content: ")

        while new_line != "stop":
            file.write(new_line + "\n")
            new_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
