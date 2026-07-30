def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    content_line = ""

    while content_line != "stop":
        content_line = input("Enter new line of content: ")
        content.append(content_line)

    with open(f"{file_name}.txt", "w") as file:
        for line in content:
            if line != "stop":
                file.write(line + "\n")
