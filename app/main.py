def main() -> None:
    file_name = input("Enter name of the file: ")

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line + "\n")

    file_full_name = f"{file_name}.txt"

    with open(file_full_name, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
