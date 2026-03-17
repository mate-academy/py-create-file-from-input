def main() -> None:
    file_name = input("Введіть ім`я файлу: ")
    content_lines = []

    while True:
        line = input("Введіть текст: ")
        if line == "stop":
            break
        content_lines.append(line + "\n")

    full_name = f"{file_name}.txt"

    with open(full_name, "w", encoding="utf-8") as file:
        file.writelines(content_lines)

    print(f"Файл '{full_name}' успішно створено!")


if __name__ == "__main__":
    main()
