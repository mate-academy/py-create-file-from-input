def main() -> None:
    name_file = input("Enter name of the file: ")
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)
    with open(name_file + ".txt", "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
