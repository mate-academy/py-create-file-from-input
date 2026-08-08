def main() -> None:
    file_name = input("Enter name of the file: ")

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    content = "\n".join(lines)

    with open(f"{file_name}.txt", "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
