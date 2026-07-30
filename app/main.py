def main() -> None:
    with open(input("Enter name of the file: ") + ".txt", "w") as user_file:
        while user_file:
            user_input = input("Enter new line of content: ")
            if user_input != "stop":
                user_file.write(user_input + "\n")
            else:
                break


if __name__ == "__main__":
    main()
