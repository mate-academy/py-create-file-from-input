def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return

    # Dodaj rozszerzenie .txt
    file_name = f"{file_name}.txt"

    lines: list[str] = []

    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    # Zapis do pliku
    with open(file_name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")

    print(f'File "{file_name}" created successfully!')


if __name__ == "__main__":
    main()
