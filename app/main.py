def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []

    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        file_content.append(text)

    with open(f"{file_name}.txt", "a") as f:
        for content in file_content:
            f.write(f"{content}\n")


if __name__ == "__main__":
    main()
