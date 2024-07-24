def main() -> None:
    name_of_file = input("Enter name of the file: ") + ".txt"
    lines = []
    new_line = input("Enter new line of content: ")

    while new_line.lower() != "stop":
        lines.append(new_line)
        new_line = input("Enter new line of content: ")

    with open(name_of_file, "a") as f:
        for line in lines:
            f.write(line)
            f.write("\n")


if __name__ == "__main__":
    main()
