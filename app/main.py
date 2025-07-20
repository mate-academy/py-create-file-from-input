def main() -> None:
    file_name = input("Enter name of the file: ")
    if file_name:
        with open(f"{file_name}.txt", "a") as record_file:
            while True:
                file_content = input("Enter new line of content: ")
                if file_content == "stop":
                    break
                record_file.write(file_content + "\n")


if __name__ == "__main__":
    main()
