def main() -> None:
    name = input("Enter name of the file: ")
    options = ""
    option = ""
    while option != "stop":
        option = input("Enter new line of content: ")
        if option != "stop":
            options += option + "\n"

    with open(name + ".txt", "w") as text_file:
        text_file.write(options)


if __name__ == "__main__":
    main()
