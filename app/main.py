def main():
    try:
        # Запитуємо у користувача ім'я файлу
        file_name = input("Enter name of the file: ").strip()
        if not file_name:
            print("File name cannot be empty.")
            return

        file_name += ".txt"

        # Відкриваємо файл для запису
        with open(file_name, "w") as f:
            while True:
                line = input("Enter new line of content: ")
                if line.lower() == "stop":
                    break
                f.write(line + "\n")

        print(f"File '{file_name}' created successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
