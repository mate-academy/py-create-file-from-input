def main() -> None:
    name = input("Enter name of the file: ")
    content_text = []
    content = input("Enter new line of content: ")
    while content != "stop":
        content_text.append(content)
        content = input("Enter new line of content: ")
    content_to_write = "\n".join(content_text)
    file_name = f"{name}.txt"
    with open(file_name, "w") as f:
        f.write(content_to_write)


if __name__ == "__main__":
    main()
