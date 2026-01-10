def main() -> None:
    input_str = input("Enter name of the file: ")
    file_name = input_str + ".txt"
    file_content = ""
    while input_str != "stop":
        input_str = input("Enter new line of content: ")
        if input_str != "stop":
            file_content += input_str + "\n"
    with open(file_name, "w") as f:
        f.write(file_content)


if __name__ == "__main__":
    main()
