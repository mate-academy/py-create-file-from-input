def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content_list = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_list.append(line)

    with open(file_name, "w") as file:
        for line in content_list:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
