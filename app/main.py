def main() -> None:
    file_name = input("Enter name of the file: ")
    open(file_name + ".txt", "a").close()

    while True:
        new_line_of_content = input("Enter new line of content: ")
        if new_line_of_content.lower() == "stop":
            break

        with open(file_name + ".txt", "a") as user_file:
            user_file.write(new_line_of_content + "\n")


if __name__ == "__main__":
    main()
