def main() -> None:
    filename = input("Enter name of the file: ")
    content = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    with open(filename + ".txt", "a") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
