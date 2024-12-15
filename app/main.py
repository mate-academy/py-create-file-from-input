def main() -> None:
    file_name = input("Enter name of the file: ")

    new_line = input("Enter new line of content: ")

    if new_line == "stop":
        with open(f"{file_name}.txt", "w"):
            pass

    while new_line != "stop":
        open_new_file = open(f"{file_name}.txt", "a")
        open_new_file.write(f"{new_line}\n")
        new_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
