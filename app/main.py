def main() -> None:
    file_name = input("Enter name of the file: ")
    list_text = []
    line = ""
    while line != "stop":
        line = input("Enter new line of content: ")
        if line != "stop":
            list_text.append(line)

    data_file_name = file_name + ".txt"
    with open(data_file_name, "a") as new_file:
        new_file.write("\n".join(list_text))


if __name__ == "__main__":
    main()
