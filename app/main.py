def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = ""
    while content != "stop" + "\n":
        with open(file_name, "a") as f:
            f.write(content)
            content = input("Enter new line of content: ") + "\n"


if __name__ == "__main__":
    main()
