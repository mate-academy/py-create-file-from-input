def main() -> None:
    name_of_file = input("Enter name of the file: ")
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)
    content = "\n".join(lines)
    with open(name_of_file + ".txt", "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
