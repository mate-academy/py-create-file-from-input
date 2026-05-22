def main() -> None:
    name1 = input("Enter name of the file: ")
    filename = name1 + ".txt"
    lines = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        lines.append(new_line)
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
