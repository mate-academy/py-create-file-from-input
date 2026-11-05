def main() -> None:
    filename: str = input("Enter name of the file: ")
    lines: list[str] = []

    while True:
        line: str = input("Enter new line of content: ")

        if line == "stop":
            break

        lines.append(line)

    with open(f"{filename}.txt", "w") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
