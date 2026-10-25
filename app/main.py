def main() -> None:
    file_name = input("Enter name of the file: ")
    file_extension = ".txt"
    file_path = file_name + file_extension
    user_input = ""
    with open(file_path, "w") as f:
        while user_input != "stop":
            user_input = input("Enter new line of content: ")
            if user_input == "stop":
                break
            f.write(user_input + "\n")


if __name__ == "__main__":
    main()
