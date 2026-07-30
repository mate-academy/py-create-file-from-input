def main() -> None:
    name_input = input("Enter name of the file: ")
    with open(f"{name_input}.txt", "a") as text_file:
        line_input = input("Enter new line of content: ")
        while line_input != "stop":
            text_file.write(f"{line_input}\n")
            line_input = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
