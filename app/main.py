def main() -> None:
    strings_list = []
    file_name = input("Enter name of the file: ")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        strings_list.append(new_line)

    with open(f"{file_name}.txt", "w") as file:
        for string in strings_list:
            file.write(string + "\n")


if __name__ == "__main__":
    main()
