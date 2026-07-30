def main() -> None:
    filename = input("Enter name of the file: ")
    with open(f"{filename}.txt", "a") as file:
        user_input = input("Enter new line of content: ")
        while user_input != "stop":
            file.writelines(f"{user_input}\n")
            user_input = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
