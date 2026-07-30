def main() -> None:
    name = input("Enter name of the file: ")
    file_name = f"{name}.txt"

    lines: list[str] = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(file_name, "w") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
