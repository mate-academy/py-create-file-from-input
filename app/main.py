def main() -> None:
    name = input("Enter name of the file: ")
    name += ".txt"

    content = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(name, "w") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
