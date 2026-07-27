def main() -> None:
    file_name = input("Enter name of the file: ")
    texts = []
    while True:
        text = input("Enter new line of content: ")
        if text.lower() == "stop":
            break
        texts.append(text)

    with open(f"{file_name}.txt", "w") as f:
        for text in texts:
            f.write(text + "\n")


if __name__ == "__main__":
    main()
