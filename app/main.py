def main() -> None:
    filename = input("Enter name of the file:") + '.txt'
    lines = []
    while True:
        content = input("Enter new line of content:")
        if content == "stop":
            break
        lines.append(content)
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
