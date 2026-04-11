def main() -> None:
    name_file = f"{input('Enter name of the file: ')}.txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)
    with open(name_file, "w") as name:
        name.write("\n".join(lines))


if __name__ == "__main__":
    main()
