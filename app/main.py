def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = f"{file_name}.txt"

    content_lines = []

    while True:
        content_line = input("Enter new line of content: ")

        if content_line.lower() == "stop":
            break

        content_lines.append(content_line)

    with open(file_name, "w") as file:
        for line in content_lines:
            file.write(line + "\n")
