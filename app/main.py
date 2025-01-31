def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "a") as file:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            file.write(f"{text}\n")  # Додаємо рядок правильно


if __name__ == "__main__":
    main()
