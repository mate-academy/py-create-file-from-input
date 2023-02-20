def main() -> None:
    name_of_the_file = input("Enter name of the file: ")
    new_file = open(f"{name_of_the_file}.txt", "a")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        else:
            new_file.write(new_line + "\n")


if __name__ == "__main__":
    main()
