def main() -> None:
    file_name = input("Enter name of the file: ")

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break

        content_lines.append(line)

    with open(f"{file_name}.txt", "w") as file:

        for line in content_lines:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
