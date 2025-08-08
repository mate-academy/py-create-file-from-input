def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return

    full_file_name = f"{file_name}.txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    with open(full_file_name, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
