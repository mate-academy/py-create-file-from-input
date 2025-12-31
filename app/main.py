def main() -> None:
    name = input("Enter name of the file: ")
    file_lines = []
    # while (content := input("Enter new line: ")) != "stop":
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        file_lines.append(line)
    # name = name + ".txt"
    with open(name + ".txt", "w") as f:
        f.write("\n".join(file_lines))


if __name__ == "__main__":
    main()
