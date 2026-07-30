def main() -> None:
    name = str(input("Enter name of the file: ") + ".txt")
    lines = []
    while name:
        line = str(input("Enter new line of content: "))
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(name, "w") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
