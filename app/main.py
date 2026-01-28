def main() -> None:
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    content_line = []
    while True:
        content = input("Enter new line of content: ")
        if content.lower() == "stop":
            break
        content_line.append(content)
    with open(file_name, "w") as f:
        for content in content_line:
            f.write(f"{content}\n")


if __name__ == "__main__":
    main()
