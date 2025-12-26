def main() -> None:
    file_name = input("Enter name of the file: ")
    content_list = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        content_list.append(new_line)

    with open(f"{file_name}.txt", "w") as file:
        for line in content_list:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
