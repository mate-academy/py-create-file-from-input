def main() -> None:
    content = ""
    file_name = input("Enter name of the file: ")

    while True:
        line_content = input("Enter new line of content: ")
        if line_content == "stop":
            break
        content += f"{line_content}\n"

    with open(f"{file_name}.txt", "w") as txt_file:
        txt_file.write(content)


if __name__ == "__main__":
    main()
