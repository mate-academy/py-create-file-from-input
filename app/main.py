def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    list_ = []
    while True:
        for_write = input("Enter new line of content: ")
        if for_write == "stop":
            break
        list_.append(for_write)

    with open(file_name, "a") as file:
        for char in list_:
            file.write(char + "\n")


if __name__ == "__main__":
    main()
