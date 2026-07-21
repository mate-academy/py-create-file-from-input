def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return
    file_name = f"{file_name}.txt"

    with open(file_name, "a", encoding="utf-8") as output_file:
        while True:
            file_line = input("Enter new line of content: ").strip()
            if file_line.lower() == "stop":
                break
            output_file.write(file_line + "\n")

    print(f'File "{file_name}" has been created successfully.')


if __name__ == "__main__":
    main()
