def main() -> None:
    name = input("Enter name of the file: ")
    lines = []
    new_line = input("Enter new line of content: ")
    while new_line != "stop":
        lines.append(new_line)
        new_line = input("Enter new line of content: ")
    name += ".txt"
    with open(name, "w") as new_file:
        for line in lines:
            new_file.write(line + "\n")


if __name__ == "__main__":
    main()
