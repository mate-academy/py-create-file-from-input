def main() -> None:
    name_of_file = input("Enter name of the file: ")
    open_file = open(f"{name_of_file}.txt", "a")
    while True:
        new_line = input("Enter new line of content: ") + "\n"
        if new_line != "stop\n":
            open_file.write(new_line)
        else:
            break


if __name__ == "__main__":
    main()
