def main() -> None:
    name = input("Enter name of the file: ")
    file_name = f"{name}.txt"
    content = []
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        content.append(text + "\n")
    with open(file_name, "a") as file:
        for i in content:
            file.write(i)


if __name__ == "__main__":
    main()
