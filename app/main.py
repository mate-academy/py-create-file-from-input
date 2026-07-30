def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line + "\n")

    open(file_name + ".txt", "w").writelines(lines)


if __name__ == "__main__":
    main()
