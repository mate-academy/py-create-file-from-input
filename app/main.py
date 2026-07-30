def main() -> None:
    file_name = input("Enter name of the file: ")
    text_list = []
    while True:
        temp_line = input("Enter new line of content: ")
        if temp_line.lower() == "stop":
            break
        text_list.append(temp_line)
    if text_list is not False:
        with open(f"{file_name}.txt", "w") as file:
            for line in text_list:
                file.write(line + "\n")


if __name__ == "__main__":
    main()
