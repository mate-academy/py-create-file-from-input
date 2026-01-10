def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = f"{file_name}.txt"
    file_data = []
    while True:
        content = input("Enter new line of content: ")
        if content.lower() == "stop":
            break
        file_data.append(content)

    with open(file_name, "w") as file:
        for content in file_data:
            file.write(content + "\n")


if __name__ == "__main__":
    main()
