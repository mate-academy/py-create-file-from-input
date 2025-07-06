def main():
    filename = input("Enter name of the file: ")

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content_lines.append(line)

    file_path = f"{filename}.txt"

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in content_lines:
            file.write(line + '\n')


if __name__ == "__main__":
    main()
