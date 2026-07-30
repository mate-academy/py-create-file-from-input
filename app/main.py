def main() -> None:
    file_name = input("Enter name of the file: ")
    list_of_line = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        list_of_line.append(line)
    with open(f"{file_name}.txt", "w") as file:
        for line in list_of_line:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
