def main():
    # Питаємо ім'я файлу
    file_name = input("Enter name of the file: ") + ".txt"

    content = []

    # Запит рядків у циклі
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    # Запис у файл
    with open(file_name, "w") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()

