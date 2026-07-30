def main(file_name: str = None) -> None:
    if file_name is None:
        file_name = input("Enter name of the file: ")
        file_name += ".txt"
    with open(file_name, "a") as file:
        while True:
            text = input("Enter new line of content: ")
            if text.lower() == "stop":
                break
            file.write(text + "\n")
