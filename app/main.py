def main() -> None:
    filename = input("Enter name of the file: ")
    document = open(f"{filename}.txt", "a")
    content = input("Enter new line of content: ")

    while content != "stop":
        document.write(content + "\n")
        content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
