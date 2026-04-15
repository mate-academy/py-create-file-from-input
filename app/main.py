def main():
    file_name = input("Enter name of the file: ")
    full_path = f"{file_name}.txt"
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content_lines.append(line)

    try:
        with open(full_path, "w", encoding="utf-8") as file:
            file.write("\n".join(content_lines))

    except Exception:
        pass


if __name__ == "__main__":
    main()
