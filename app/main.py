import os


def get_file_name() -> str:
    while True:
        file_name = input("Enter name of the file: ")
        full_file_name = file_name + ".txt"

        if os.path.exists(full_file_name):
            print(f"Файл '{full_file_name}' уже существует.")
            overwrite = input("Wanted rewrite file?").strip().lower()
            if overwrite == "да":
                return full_file_name
        else:
            return full_file_name


def main() -> None:
    full_file_name = get_file_name()

    content = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(full_file_name, "w") as file:
        for line in content:
            file.write(line + "\n")

    print(f"Файл '{full_file_name}' был успешно создан и заполнен.")


if __name__ == "__main__":
    main()
