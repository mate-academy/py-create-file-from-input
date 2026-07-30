def main() -> None:
    name = input("Enter name of the file: ")
    lines = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        lines += [new_line + "\n"]
    with open(name + ".txt", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
