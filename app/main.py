def main() -> None:
    file_name_input = input("Enter name of the file: ")
    file_name_input += ".txt"

    with open(file_name_input, "a") as file:
        while True:
            new_line_input = input("Enter new line of content: ")
            if new_line_input.lower() == "stop":
                break
            else:
                file.write(new_line_input + "\n")


if __name__ == "__main__":
    main()
