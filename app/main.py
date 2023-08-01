def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    data_for_file = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        data_for_file.append(content)

    with open(file_name, "a") as f:
        for string in data_for_file:
            f.write(string + "\n")

    with open(file_name, "r") as f:
        print(f.readlines())


if __name__ == "__main__":
    main()
