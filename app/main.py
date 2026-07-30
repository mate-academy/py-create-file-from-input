def main() -> None:
    """
    Створює текстовий файл з назвою та вмістом, введеними користувачем.
    """

    file_name = input("Enter name of the file: ")
    file_name_with_extension = file_name + ".txt"
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    try:
        with open(file_name_with_extension, "w") as file:
            for line in content_lines:
                file.write(line + "\n")
        print(f"File '{file_name_with_extension}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
