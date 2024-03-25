def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    file_content = ""
    user_input = None
    while user_input != "stop":
        user_input = input("Enter new line of content: ")
        if user_input != "stop":
            file_content += user_input + "\n"

    with open(file_name, "w") as file:
        file.write(file_content)

        print(f"The file '{file_name}' "
              f"has been created and filled with the provided content.")


if __name__ == "__main__":
    main()
