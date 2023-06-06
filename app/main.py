def main() -> None:
    file_name = f"{input('Enter name of the file: ')}.txt"
    lines: list[str] = []
    while True:
        current = input("Enter new line of content: ")
        if current == "stop":
            break
        lines.append(current + "\n")
    with open(file_name, "w") as handle:
        handle.writelines(lines)


if __name__ == "__main__":
    main()
