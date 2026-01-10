def main() -> None:
    file_name = input("Enter name of the file: ")

    while True:
        with open(file_name + ".txt", "a+") as file:
            user_input = input("Enter new line of content: ")
            if user_input == "stop":
                break
            file.write(user_input + "\n")


if __name__ == "__main__":
    main()
