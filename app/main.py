def main() -> None:
    file_name = input("Enter name of the file: ")
    list_of_content = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        list_of_content.append(content)

    with open(f"{file_name}.txt", "a") as f:
        for line in list_of_content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
