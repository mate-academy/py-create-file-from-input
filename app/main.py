def main() -> None:
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    with open(file_name, "w") as file:
        while True:
            user_input = input("Enter new line of content: ")

            if user_input == "stop":
                break

            file.write(user_input + "\n")


if __name__ == "__main__":
    main()
