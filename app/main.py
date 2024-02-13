def main() -> None:
    file_list = []
    name_file = input("Enter name of the file: ")
    while True:
        text_file = input("Enter new line of content: ")

        if text_file == "stop":
            break
        file_list.append(text_file)
    with open(f"{name_file}.txt", "a") as f:
        for i in file_list:
            f.write(i + "\n")


if __name__ == "__main__":
    main()
