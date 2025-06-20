def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []

    while True:
        content_line = input("Enter new line of content: ")
        if content_line.lower() == "stop":
            break
        lines.append(content_line)

    with open(f"{file_name}.txt", "w") as file:
        for line in lines:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
