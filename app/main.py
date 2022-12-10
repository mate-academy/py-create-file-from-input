def main() -> None:
    file_name = input("Enter name of the file: ")
    list_of_content = []
    while True:
        line_of_content = input("Enter new line of content: ")
        if line_of_content == "stop":
            break
        list_of_content.append(line_of_content)
    with open(f"{file_name}.txt", "w") as file:
        for line in list_of_content:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
