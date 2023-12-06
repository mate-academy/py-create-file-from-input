def main() -> None:
    file_name = input("Enter name of the file: ")
    result_str = []
    while True:
        string = input("Enter new line of content: ")
        if string == "stop":
            break
        result_str.append(string)
    with open(file_name + ".txt", "w") as file:
        for line in result_str:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
