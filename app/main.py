def main() -> None:
    file_name = input("Enter name of the file: ")

    content_lines = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        content_lines.append(new_line)

    with open(f"{file_name}.txt", "w") as f:
        for new_line in content_lines:
            f.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
