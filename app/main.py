def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []

    while True:
        next_line = input("Enter new line of content: ")
        if next_line == "stop":
            break
        content.append(next_line)

    content_data = "\n".join(content)

    with open(f"{file_name}.txt", "w") as file:
        file.write(content_data)


if __name__ == "__main__":
    main()
