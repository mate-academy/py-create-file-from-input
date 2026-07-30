def main() -> None:
    file_name = input("Enter name of the file: ")
    app_atributes = []
    while True:
        enter_line = input("Enter new line of content: ")
        if enter_line.lower() == "stop":
            break
        app_atributes.append(enter_line)

    full_file_name = file_name + ".txt"
    try:
        with open(full_file_name, "w") as file:
            for item in app_atributes:
                file.write(item + "\n")
        print(f"Файл '{full_file_name}' успішно створено.")
    except Exception as e:
        print(f"Виникла помилка при створенні файлу: {e}")


if __name__ == "__main__":
    main()
