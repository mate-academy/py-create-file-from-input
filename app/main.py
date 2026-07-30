def main() -> None:
    file_name = input("Enter name of the file: ")

    open(file_name + ".txt", "w").close()
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        with open(file_name + ".txt", "a") as file:
            file.write(user_input + "\n")


if __name__ == "__main__":
    main()
