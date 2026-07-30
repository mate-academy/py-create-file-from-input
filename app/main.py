def get_user_input() -> str:
    """Отримує ім'я файлу від користувача."""
    file_name: str = input("Enter name of the file: ")
    return f"{file_name}.txt"


def get_file_content() -> list[str]:
    """Отримує вміст файлу від користувача до слова 'stop'."""
    content: list[str] = []
    while True:
        line: str = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)
    return content


def write_to_file(file_name: str, content: list[str]) -> None:
    """Записує вміст у файл."""
    with open(file_name, mode="w", encoding="utf-8") as file:
        for line in content:
            file.write(f"{line}\n")


def main() -> None:
    """Головна функція для створення файлу з вмістом."""
    file_name: str = get_user_input()
    content: list[str] = get_file_content()
    write_to_file(file_name, content)


if __name__ == "__main__":
    main()
