def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    file_content = ""

    while file_content != "stop":
        with open(file_name, "a") as file:
            file_content = input("Enter new line of content: ")
            if file_content != "stop":
                file.write(file_content + "\n")


if __name__ == "__main__":
    main()
