def main() -> None:
    name_file = input("Enter name of the file: ") + ".txt"
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        else:
            content.append(line)

    with open(name_file, "w") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
