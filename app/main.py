def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []

    while True:
        enter_line = input("Enter new line of content: ")
        if enter_line.lower().strip() == "stop":
            break
        lines.append(enter_line)

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    with open(file_name, "w") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
