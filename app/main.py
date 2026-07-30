def main() -> None:
    file_name = input("Enter name of the file: ", ) + ".txt"
    current_file = open(file_name, "a")
    exit_word = True
    while exit_word is True:
        new_line = input("Enter new line of content: ", )
        if new_line != "stop":
            current_file.write(f"{new_line}\n")
        else:
            exit_word = False
    current_file.close()


if __name__ == "__main__":
    main()
