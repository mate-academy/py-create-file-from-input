def main() -> None:
    file_name = input("Enter name of the file: ").strip() + ".txt"
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(file_name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")

    print(f'File "{file_name}" created successfully.')


if __name__ == "__main__":
    main()
