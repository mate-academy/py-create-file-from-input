def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    full_path = f"{file_name}.txt"

    with open(full_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))


if __name__ == "__main__":
    main()
