def main() -> None:
    user_input = input("Enter name of the file: ")
    file_name = f"{user_input}.txt"
    file_content = ""
    user_input = input("Enter new line of content: ")
    while user_input != "stop":
        file_content += f"{user_input}\n"
        user_input = input("Enter new line of content: ")
    file_content = file_content.strip()
    with open(file_name, "w") as f:
        f.write(file_content)


if __name__ == "__main__":
    main()
