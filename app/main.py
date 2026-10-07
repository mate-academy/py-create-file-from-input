def main() -> None:
    file_name = input("Enter name of the file: ")
    text_of_user = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        text_of_user.append(new_line)
    full_file_name = file_name + ".txt"
    with open(full_file_name, "w") as file:
        file.write("\n".join(text_of_user))


if __name__ == "__main__":
    main()
