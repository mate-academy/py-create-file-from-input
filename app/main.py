def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    list_of_content = []
    while True:
        line = input("Enter new line of content: ")
        if line != "stop":
            list_of_content.append(line)
        else:
            break

    with open(file_name, "a") as file:
        for line in list_of_content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
