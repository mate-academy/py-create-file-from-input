def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = file_name + ".txt"
    content = ""

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content = content + line + "\n"

    with open(file_name, "w") as file:
        file.write(content)
