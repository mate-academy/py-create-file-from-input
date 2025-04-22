def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"  # Ensure `.txt` extension
    with open(file_name, "a") as file:
        while True:
            input_content = input("Enter new line of content: ")
            if input_content.lower() == "stop":
                break
            file.write(input_content + "\n")

    print(f'File "{file_name}" created successfully.')


if __name__ == "__main__":
    main()
