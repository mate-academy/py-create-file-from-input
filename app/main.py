def main() -> None:
    stop = False
    content = []

    filename = input("Enter name of the file: ")
    if not filename.endswith(".txt"):
        filename += ".txt"

    while not stop:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            stop = True
        else:
            content.append(line)

    with open(filename, "w") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
