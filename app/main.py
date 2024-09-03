def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    content_words = []

    while True:
        file_content = input("Enter new line of content: ")
        if file_content.lower() == "stop":
            break
        content_words.append(file_content)

    with open(file_name, "w") as file_1:
        for char in content_words:
            file_1.write(char + "\n")

    print(f"File name: {file_name}", end="")
    print("File content:", end="")
    for line in content_words:
        print(line)


if __name__ == "__main__":
    main()
