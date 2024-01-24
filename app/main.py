def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "a") as new_file:
        new_file.write("")

        while True:
            file_content = input("Enter new line of content: ")

            if file_content.lower() == "stop":
                break
            new_file.write(file_content + "\n")


if __name__ == "__main__":
    main()
