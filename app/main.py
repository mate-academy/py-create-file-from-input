def main() -> None:
    user_file_name = input("Enter name of the file: ")
    user_file_entry = ""
    program_working = True

    while program_working:
        user_input = input("Enter new line of content: ")

        if user_input == "stop":
            program_working = False
        else:
            user_file_entry += user_input + "\n"

    with open(f"{user_file_name}.txt", "w") as f:
        f.write(user_file_entry)


if __name__ == "__main__":
    main()
