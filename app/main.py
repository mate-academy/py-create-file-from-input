def main() -> None:

    file_name = input("Enter name of the file: ")

    with open(file_name + ".txt", "a") as new_file:
        user_string = ""
        while user_string != "stop":
            if user_string:
                new_file.write(user_string + "\n")
            user_string = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
