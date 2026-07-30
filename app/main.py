def main() -> None:
    filename = input("Enter name of the file: ")
    content = []
    text = ""

    while text != "stop":
        text = input("Enter new line of content: ")
        if text != "stop":
            content.append(text)

    filename_file = open(f"{filename}.txt", "a")

    for line in content:
        filename_file.write(f"{line}\n")

    filename_file.close()


if __name__ == "__main__":
    main()
