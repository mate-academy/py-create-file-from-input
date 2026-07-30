def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    lines = []
    while True:
        text = input("Enter new line of content: ")
        if text.lower() == "stop":
            break
        lines.append(text)

    with open(file_name, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
