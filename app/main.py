def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, "w") as file:
        input_text = ""
        input_line = ""
        while input_line != "stop":
            input_line = input("Enter new line of content: ")
            if input_line != "stop":
                input_text += input_line + "\n"
        file.write(input_text)


if __name__ == "__main__":
    main()
