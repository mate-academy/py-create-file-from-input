def main() -> None:
    file_name = input("Enter name of the file: ")
    text: list[str] = []
    line = ""

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        text.append(line)

    with open(file_name + ".txt", "w+") as f:
        f.write("\n".join(text))


if __name__ == "__main__":
    main()
