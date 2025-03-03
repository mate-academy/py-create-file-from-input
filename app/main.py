def main() -> None:

    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w"):
        pass

    while True:
        user_input = input("Enter new line of content: ")

        if user_input.lower() == "stop":
            break

        with open(f"{file_name}.txt", "a") as file_content:
            file_content.write(user_input + "\n")


if __name__ == "__main__":
    main()
