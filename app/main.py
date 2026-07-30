def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    new_list = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break

        new_list.append(line)

    with open(file_name, "w") as file:
        for line in new_list:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
