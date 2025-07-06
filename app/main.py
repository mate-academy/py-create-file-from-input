def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    file_content = []
    user_input = None
    while user_input != "stop":
        user_input = input("Enter new line of content: ")
        if user_input != "stop":
            file_content.append(user_input)

    with open(file_name, "w") as file:
        for line in file_content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
