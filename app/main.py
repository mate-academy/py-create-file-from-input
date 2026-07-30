def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file:
        content = input("Enter new line of content: ")
        while not content == "stop":
            file.write(content + "\n")
            content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
