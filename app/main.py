def main() -> None:
    input_list = []
    file_name = input("Enter name of the file: ")

    value = ""
    while value != "stop":
        if value:
            input_list.append(value)
        value = input("Enter new line of content: ")

    with open(file_name + ".txt", "w") as fo:
        for item in input_list:
            fo.write(item + "\n")


if __name__ == "__main__":
    main()
