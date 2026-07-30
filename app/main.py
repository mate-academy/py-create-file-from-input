def main() -> None:
    name_file = input("Enter name of the file: ")
    if not name_file.endswith(".txt"):
        name_file += ".txt"
    check = True
    with open(name_file, "w") as file:
        while check:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                check = False
            else:
                file.write(new_line + "\n")


if __name__ == "__main__":
    main()
