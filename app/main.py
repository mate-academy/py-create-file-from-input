class EmptyFilenameError(Exception):
    pass


def main() -> None:
    filename = input("Enter name of the file: ")
    if not filename:
        raise EmptyFilenameError("Filename must be not empty")
    content = ""
    while True:
        input_text = input("Enter new line of content: ")
        if input_text == "stop":
            break
        content += input_text + "\n"

    with open(f"{filename}.txt", "w") as file_:
        file_.write(content)


if __name__ == "__main__":
    while True:
        try:
            main()
        except EmptyFilenameError:
            continue
        else:
            break
