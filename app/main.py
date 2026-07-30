def main() -> None:
    filename = input("Enter name of the file: ")
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)
    with open(filename + ".txt", "w") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
