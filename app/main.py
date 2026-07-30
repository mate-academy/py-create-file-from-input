def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content_list = []

    if file_name:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line.lower() == "stop":
                break
            file_content_list.append(new_line)

    with open(f"{file_name}.txt", "w") as input_file:
        if file_content_list:
            input_file.write("\n".join(file_content_list))


if __name__ == "__main__":
    main()
