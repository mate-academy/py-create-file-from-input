def main() -> None:
    file_name = str(input("Enter name of the file: "))
    content = str(input("Enter new line of content: "))

    with open(file_name + ".txt", "a") as file:
        while content.lower() != "stop":
            file.write(content + "\n")
            content = str(input("Enter new line of content: "))


if __name__ == "__main__":
    main()
