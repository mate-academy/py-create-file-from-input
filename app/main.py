def main() -> None:
    name = input("Enter name of the file: ")
    lines = []
    new_line = ""

    while new_line != "stop":
        new_line = input("Enter new line of content: ")
        if new_line != "stop":
            lines += f"{new_line}\n"

    with open(f"{name}.txt", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
