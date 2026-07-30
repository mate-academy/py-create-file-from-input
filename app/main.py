def main() -> None:
    name = input("Enter name of the file: ")
    filename = name + ".txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            lines.append(line + "\n")
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
