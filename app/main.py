def main() -> None:
    file_name = input("Enter name of the file: ")
    content = input("Enter new line of content: ")
    with open(f"{file_name}.txt", "a") as created_file:
        while content != "stop":
            created_file.write(content + "\n")
            content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
