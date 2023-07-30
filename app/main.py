def main() -> None:
    f_name = input("Enter name of the file: ") + ".txt"
    user_text = ""
    user_input = input("Enter new line of content: ")
    while user_input != "stop":
        user_text += user_input + "\n"
        user_input = input("Enter new line of content: ")

    with open(f_name, "w") as file:
        file.write(user_text)


if __name__ == "__main__":
    main()
