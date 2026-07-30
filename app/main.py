def main() -> None:
    file_name = input("Enter name of the file: ")
    text = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        else:
            text.append(content)
    with open(f"{file_name}.txt", "a") as file:
        for line in text:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
