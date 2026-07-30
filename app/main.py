def main() -> None:
    file_name = input("Enter name of the file: ")
    content = ""

    while True:
        content_line = input("Enter new line of content: ")
        if content_line == "stop":
            break
        content += f"{content_line}\n"

    with open(f"{file_name}.txt", "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
