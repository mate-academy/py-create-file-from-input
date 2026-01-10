def main() -> None:
    name_file = input("Enter name of the file: ")
    with open(name_file + ".txt", "w") as file_open:
        while True:
            input_text = input("Enter new line of content: ")
            if input_text == "stop":
                break
            file_open.write(input_text + "\n")


if __name__ == "__main__":
    main()
