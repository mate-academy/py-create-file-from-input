def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, 'a') as file:
        while True:
            file_content = input("Enter new line of content: ")

            if file_content == "stop":
                break
            file.write(file_content + "\n")


if __name__ == "__main__":
    main()
