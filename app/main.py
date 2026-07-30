def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(name, "w") as f:
        for line in content_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
