def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    user_content = ""
    whole_file = ""
    while user_content != "stop":
        user_content = input("Enter new line of content: ")
        if user_content != "stop":
            whole_file += user_content + "\n"
    with open(file_name, "w") as f:
        f.write(whole_file)


if __name__ == "__main__":
    main()
