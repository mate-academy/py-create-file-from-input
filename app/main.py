def main() -> None:
    name = input("Enter name of the file: ").strip() + ".txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line + "\n")

    with open(name, "w") as file:
        for line in lines:
            file.write(line)


if __name__ == "__main__":
    main()
