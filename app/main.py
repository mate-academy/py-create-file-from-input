def main() -> None:
    file_name = input("Enter name of the file: ")
    content = ""
    while (content_input := input("Enter new line of content: ")) != "stop":
        content += content_input + "\n"

    with open(file_name + ".txt", "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
