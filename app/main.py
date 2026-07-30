def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    print(f'File "{filename}" has been created.')
    pass


if __name__ == "__main__":
    main()
