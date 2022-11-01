def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    file_content = ""
    text = None
    while text != "stop":
        if text is not None:
            file_content += text + "\n"
        text = input("Enter new line of content: ")

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(file_content)
    print(f"File {file_name} was created")


if __name__ == "__main__":
    main()
