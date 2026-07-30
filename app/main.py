def main() -> None:
    file_name = input("Enter name of the file: ")
    text = ""

    while True:
        input_line = input("Enter new line of content: ")
        if input_line.lower() == "stop":
            break
        text += f"{input_line}\n"

    new_file = open(str(file_name + ".txt"), "w")
    new_file.write(text)
    new_file.close()


if __name__ == "__main__":
    main()
