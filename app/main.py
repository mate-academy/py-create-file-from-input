def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as file:
        while True:
            content = input("Enter new line of content: ")
            if content.lower() == "stop":
                break
            file.write(content + "\n")


if __name__ == "__main__":
    main()
