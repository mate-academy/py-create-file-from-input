def main():
    file_name = input("Enter name of the file: ") + ".txt"
    content_list = []

    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        content_list.append(content)

    with open(file_name, "x") as file:
        for line in content_list:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
