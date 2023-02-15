def main() -> None:
    name = input("Enter name of the file: ")
    file_content = ""
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        file_content += content + "\n"
    file_user = open(f"{name}.txt", "w")
    file_user.write(file_content)
    file_user.close()
