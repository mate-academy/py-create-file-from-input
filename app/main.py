def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    full_users_content = ""
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        full_users_content += content + "\n"

    with open(file_name, "w") as file:
        file.write(full_users_content)


if __name__ == "__main__":
    main()
