def main() -> None:
    file_name = input("Enter name of the file: ")
    correct_file_name = f"{file_name}.txt"

    list_of_content = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        list_of_content.append(new_line)

    with open(correct_file_name, "w") as user_file:
        if list_of_content:
            for new_line in list_of_content:
                user_file.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
