def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name_str = file_name + ".txt"
    file_txt = open(file_name_str, "w")

    content = []
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        content.append(user_input)

    for line in content:
        file_txt.write(line + "\n")
    file_txt.close()


if __name__ == "__main__":
    main()
