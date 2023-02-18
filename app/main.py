def main() -> None:
    file_name = input("Enter name of the file: ")
    user_input_content = []

    while True:
        new_line_content = input("Enter new line of content: ") + "\n"
        if new_line_content.strip() == "stop":
            break
        user_input_content.append(new_line_content)

    with open(f"{file_name}.txt", "w") as file_:
        file_.writelines(user_input_content)


if __name__ == "__main__":
    main()
