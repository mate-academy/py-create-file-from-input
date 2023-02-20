def main() -> None:
    name = input("Enter name of the file: ")
    content = ""
    while True:
        user_content = input("Enter new line of content: ")
        if user_content == "stop":
            break
        content += user_content + "\n"

    with open(name + ".txt", "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
