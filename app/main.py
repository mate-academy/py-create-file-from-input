def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = ""

    while True:
        content_line = input("Enter new line of content: ")

        if content_line.lower() == "stop":
            break
        else:
            file_content += f"{content_line}\n"

    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)


if __name__ == "__main__":
    main()
