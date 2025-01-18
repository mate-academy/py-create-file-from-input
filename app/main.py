def main() -> None:
    file_name = input("Enter file name: ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"
    content_lines = []

    while True:
        line = input("Enter next line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(file_name, "w") as file:
        file.write("\n".join(content_lines))


if __name__ == "__main__":
    main()
