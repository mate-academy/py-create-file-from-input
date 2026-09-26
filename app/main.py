def main() -> None:
    name = input("Enter name of the file: ")
    user_inputing = True
    with open(name + ".txt", "a") as f:
        while user_inputing:
            user_input = input("Enter new line of content: ")
            if user_input == "stop":
                user_inputing = False
            else:
                f.write(f"{user_input}\n")


if __name__ == "__main__":
    main()
