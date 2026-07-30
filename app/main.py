def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    file_path = f"{file_name}.txt"
    file_content = "\n".join(lines)

    with open(file_path, "w") as file:
        file.write(file_content)


if __name__ == "__main__":
    main()
