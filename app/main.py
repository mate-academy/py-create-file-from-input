def main() -> None:
    file_name = input("Enter name of the file: ")
    main_file = open(f"{file_name}.txt", "a")
    next_line = input("Enter new line of content: ")
    while next_line != "stop":
        main_file.write(f"{next_line}\n")
        next_line = input("Enter new line of content: ")
    main_file.close()


if __name__ == "__main__":
    main()
