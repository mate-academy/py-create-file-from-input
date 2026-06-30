def main() -> None:
    user_file_name = input("Enter name of the file: ")

    with open(user_file_name + ".txt", "w") as file:
        user_input = input("Enter new line of content: ")
        while user_input != "stop":
            file.write(user_input + "\n")
            user_input = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
