def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = f"{file_name}.txt"

    with open(file_name, "w") as user_file:
        user_text = ""
        while user_text != "stop":
            user_text = input("Enter new line of content: ")
            if user_text != "stop":
                user_file.write(f"{user_text}\n")


if __name__ == "__main__":
    main()
