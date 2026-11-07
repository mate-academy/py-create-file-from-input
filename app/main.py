def main() -> None:
    input_file_name = input("Enter name of the file: ") + ".txt"
    file_content = ""
    input_file_content = ""
    while input_file_content != "stop":
        input_file_content = input("Enter new line of content: ")
        if input_file_content != "stop":
            file_content += input_file_content + "\n"
    output_file = open(input_file_name, "w")
    output_file.write(file_content)


if __name__ == "__main__":
    main()
