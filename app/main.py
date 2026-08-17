def main() -> None:
    file_name = input("Enter name of the file: ")
    result = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        result.append(content)
    with open(file_name + ".txt", "w") as file:
        for content in result:
            file.write(content + "\n")


if __name__ == "__main__":
    main()
