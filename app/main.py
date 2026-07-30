def main() -> None:
    name_of_the_file = input("Enter name of the file: ")
    message_list = []
    while True:
        new_line_of_content = input("Enter new line of content: ")
        if new_line_of_content.lower() == "stop":
            break
        message_list.append(new_line_of_content)
    with open(name_of_the_file + ".txt", "w") as file:
        if message_list:
            file.write("\n".join(message_list) + "\n")
        file.write("")


if __name__ == "__main__":
    main()
