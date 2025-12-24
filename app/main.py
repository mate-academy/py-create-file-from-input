def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    content = ""
    while True:
        message = input("Enter new line of content: ")
        if message == "stop":
            break
        else:
            content += message + "\n"
    with open(name, "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
