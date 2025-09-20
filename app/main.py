def main():
    # Запитуємо у користувача ім'я файлу
    file_name = input("Enter name of the file: ") + ".txt"
    content = []

    # Збираємо рядки до введення 'stop'
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    # Записуємо рядки у файл
    with open(file_name, "w") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
