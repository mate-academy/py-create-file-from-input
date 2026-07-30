def main() -> None:
    file_name = input("Enter name of the file: ")
    data_list = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        data_list.append(new_line)

    with open(file_name + ".txt", "w") as data_file:
        for line in data_list:
            data_file.write(line + "\n")


if __name__ == "__main__":
    main()
