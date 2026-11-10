def main() -> None:
    user_input = input("Enter name of the file: ")
    open_file = open(user_input + ".txt", "a")
    while user_input != "stop":
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        open_file.write(user_input + "\n")

    open_file.close()


if __name__ == "__main__":
    main()
