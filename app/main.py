def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        user_input += "\n"
        content.append(user_input)
    with open(file_name + ".txt", "w") as f:
        f.writelines(content)


if __name__ == "__main__":
    main()
