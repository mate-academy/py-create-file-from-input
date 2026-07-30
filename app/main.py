def main() -> None:
    content = []
    filename = input("Enter name of the file: ")
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        content.append(text)

    with open(filename + ".txt", "w") as file:
        for line in content:
            file.write(line + "\n")
