def main() -> None:
    name = input("Enter name of the file: ")
    content = []
    while True:
        content_line = input("Enter new line of content: ")
        if content_line == "stop":
            break
        content.append(content_line + "\n")

    with open(name + ".txt", "w") as f:
        for line in content:
            f.write(line)


if __name__ == "__main__":
    main()
