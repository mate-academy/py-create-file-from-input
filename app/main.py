def main() -> None:
    name_of_file = input("Enter name of the file: ") + ".txt"
    new_file = open(name_of_file, "a")
    while True:
        str_of_text = input("Enter new line of content: ")
        if str_of_text == "stop":
            new_file.close()
            break
        new_file.write(str_of_text + "\n")


if __name__ == "__main__":
    main()
