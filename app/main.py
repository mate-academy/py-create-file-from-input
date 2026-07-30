def main() -> None:
    file_name = input("Enter name of the file: ").strip() + ".txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    with open(file_name, "w") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
