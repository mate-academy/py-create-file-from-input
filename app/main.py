def main():
    # Крок 1: ім'я файлу
    file_name = input("Enter name of the file: ") + ".txt"

    # Крок 2: збираємо рядки
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    # Крок 3: записуємо у файл
    with open(file_name, "w") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
