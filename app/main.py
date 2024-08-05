def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    line_content = ""
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        line_content += line + "\n"
    with open(file_name, "w") as new_file:
        new_file.write(line_content)
