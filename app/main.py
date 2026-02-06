def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    lines = []

    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        lines.append(text)

    with open(file_name, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
