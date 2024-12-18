def main() -> None:
    with open(input("Enter name of the file: ") + ".txt", "a") as file:
        content = input("Enter new line of content: ")
        while content != "stop":
            file.write(content + "\n")
            content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
