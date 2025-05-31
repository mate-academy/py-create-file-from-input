def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    with open(f"{file_name}.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
