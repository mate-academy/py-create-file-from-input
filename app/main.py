def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    lines = []
    while True:
        next_line = input("Enter new line of content: ")
        if next_line == "stop":
            break
        lines.append(next_line)
    with open(file_name, "a") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
