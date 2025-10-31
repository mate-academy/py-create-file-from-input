def main() -> None:
    name = input("Enter name of the file: ")
    if not name:
        print("File name cannot be empty.")
        return

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line + "\n")

    with open(f"{name}.txt", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
