def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line + "\n")
    with open(file_name + ".txt", "a+") as file:
        file.writelines(lines)


if __name__ == "__main__":
    main()
