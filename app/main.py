def main() -> None:
    while True:
        file_name = input("Enter name of the file: ")
        if file_name.strip():
            break
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "w", encoding="utf-8") as f:
        f.write("\n".join(content))


if __name__ == "__main__":
    main()
