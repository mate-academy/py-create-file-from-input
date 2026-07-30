def main() -> None:
    file_name = input("Enter name of the file: ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":  # завершаем цикл при вводе "stop"
            break
        content_lines.append(line)

    with open(file_name, "w", encoding="utf-8") as f:
        for line in content_lines:
            f.write(line + "\n")

    print(f"File '{file_name}' created successfully with "
          f"{len(content_lines)} lines.")


if __name__ == "__main__":
    main()
