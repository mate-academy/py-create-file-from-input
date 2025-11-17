def main() -> None:
    file_name = input("Enter name of the file: ")

    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    full_file_name = file_name + ".txt"

    with open(full_file_name, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
