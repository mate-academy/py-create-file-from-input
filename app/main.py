def main() -> None:
    filename = input("Enter name of the file: ")

    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    full_filename = f"{filename}.txt"

    with open(full_filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
