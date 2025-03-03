def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    list = []
    while True:
        for_write = input("Enter new line of content: ")
        if for_write == "stop":
            break
        list.append(for_write)

    with open(file_name, "a") as file:
        for char in list:
            file.write(char + "\n")


if __name__ == "__main__":
    main()
