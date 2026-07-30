def main() -> None:
    file_name = input("Enter name of the file: ")
    empty_list = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            empty_list.append(line)
    new_file = open(f"{file_name}.txt", "w")
    for line in empty_list:
        new_file.write(line + "\n")
    new_file.close()


if __name__ == "__main__":
    main()
