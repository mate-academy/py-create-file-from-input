def main() -> None:
    name = input("Enter name of the file: ")
    filename = name + ".txt"

    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(filename, "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
