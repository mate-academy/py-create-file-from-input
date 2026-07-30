def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    while True:
        file_content = input("Enter new line of content: ")
        if file_content == "stop":
            break
        content.append(file_content)

    with open(f"{file_name}.txt", "w") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
