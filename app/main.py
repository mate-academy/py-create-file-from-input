def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []

    while (line := input("Enter new line of content: ")) != "stop":
        lines.append(line + "\n")

    open(f"{file_name}.txt", "w").writelines(lines)


if __name__ == "__main__":
    main()
