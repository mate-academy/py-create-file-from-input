def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    next_line = input("Enter new line of content: ")
    lines = []

    while next_line != "stop":
        lines.append(next_line)
        next_line = input("Enter new line of content: ")
        if lines == "stop":
            break

    with open(name, "a") as file:
        for line in lines:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
