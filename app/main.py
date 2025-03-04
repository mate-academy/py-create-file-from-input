def main() -> None:
    input_name = input("Enter name of the file: ")
    file_name = f"{input_name}.txt"

    with open(file_name, "w") as file:
        user_input = input("Enter new line of content: ")

        while user_input != "stop":
            file.write(user_input + "\n")
            user_input = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
