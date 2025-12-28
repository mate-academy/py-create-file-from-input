def main() -> None:
    name = input("Enter name of the file: ")
    if not name.endswith(".txt"):
        name += ".txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(name, "w") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
