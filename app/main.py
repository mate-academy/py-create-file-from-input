def main() -> None:
    file_name = input("Enter name of the file: ")
    content_lines = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        else:
            content_lines.append(f"{content}\n")

    file_name = f"{file_name}.txt"
    with open(file_name, "a") as f:
        f.writelines(content_lines)


if __name__ == "__main__":
    main()
