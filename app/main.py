def main() -> None:
    file_name = input("Enter name of the file: ")

    lines = []
    while True:
        first_line = input("Enter new line of content: ")
        if first_line == "stop":
            break
        lines.append(first_line)

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    with open(file_name, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
