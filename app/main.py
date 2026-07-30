def main() -> None:
    name = input("Enter name of the file: ")
    with open(name + ".txt", "w") as f:
        while True:
            content = input("Enter new line of content: ")
            if content.lower() == "stop":
                break
            f.write(content + "\n")
