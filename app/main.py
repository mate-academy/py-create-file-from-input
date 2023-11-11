def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        user_data = input("Enter new line of content: ")
        while user_data != "stop":
            file.write(user_data + "\n")
            user_data = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
