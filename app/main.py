def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    full_name = f"{file_name}.txt"

    with open(full_name, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    print(f'File "{full_name}" has been created successfully!')


if __name__ == "__main__":
    main()
