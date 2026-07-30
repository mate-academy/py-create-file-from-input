def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    content = []
    line = None
    while line != "stop":
        line = input("Enter new line of content: ")
        if line != "stop":
            content.append(line + "\n")
    with open(name, "a") as file:
        for line in content:
            file.write(line)


if __name__ == "__main__":
    main()
