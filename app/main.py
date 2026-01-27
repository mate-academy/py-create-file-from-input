def main() -> None:
    file_name = input("Enter name of the file: ")
    content = input("Enter new line of content: ")

    with open(file_name + ".txt", "w") as file:
        while content != "stop":
            file.write(content + "\n")
            content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
