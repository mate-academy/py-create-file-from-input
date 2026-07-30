def main() -> None:
    name = input("Enter name of the file: ")
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)
    filename = name + ".txt"
    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")

    print(f"Файл '{filename}' успішно збережено!")


if __name__ == "__main__":
    main()
