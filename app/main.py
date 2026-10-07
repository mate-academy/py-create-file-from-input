def main() -> None:
    name = input("Enter name of the file: ")
    next_lines = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        else:
            next_lines.append(f"{new_line}\n")

    with open(f"{name}.txt", "w") as f:
        for line in next_lines:
            f.write(line)
    pass


if __name__ == "__main__":
    main()
