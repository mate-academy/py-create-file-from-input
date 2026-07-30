def main() -> any:
    file_name = input("Enter name of the file: ")
    lines = []
    line = input("Enter new line of content: ")
    while line != "stop":
        lines.append(line)
        line = input("Enter new line of content: ")
    lines_to_write = "\n".join(lines)
    with open(file_name + ".txt", "w") as f:
        f.write(lines_to_write)


if __name__ == "__main__":
    main()
