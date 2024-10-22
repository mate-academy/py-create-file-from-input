def main() -> None:
    file_name = input("Enter name of the file: ")
    string_list = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        string_list.append(line)

    with open(file_name + ".txt", "a") as f:
        for line in string_list:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
