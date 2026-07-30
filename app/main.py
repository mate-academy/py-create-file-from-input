def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "a") as file:
        user_input = ""
        while user_input != "stop":
            user_input = input("Enter new line of content: ")
            if user_input != "stop":
                file.write(f"{user_input}\n")


if __name__ == "__main__":
    main()
