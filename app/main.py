def main() -> None:
    file_name = input("Enter name of the file: ")
    content_list = []

    while True:
        line = input("Enter new line of content: ")

        if line == "stop":
            break

        content_list.append(line)

    full_name = file_name + (".txt")

    with open(full_name, "w") as file:
        for line in content_list:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
