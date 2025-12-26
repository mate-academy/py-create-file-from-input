def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    user_text = None
    user_text_list = []
    while user_text != "stop":
        user_text = input("Enter new line of content: ")
        if user_text != "stop":
            user_text_list.append(user_text)

    with open(file_name, "w") as f:
        for line in user_text_list:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
