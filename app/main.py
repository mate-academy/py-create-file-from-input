def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, "a") as created_file:
        while True:
            file_text = input("Enter new line of content: ")
            if file_text == "stop":
                break
            else:
                created_file.write(f"{file_text}\n")


if __name__ == "__main__":
    main()
