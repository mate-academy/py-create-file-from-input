def main() -> None:
    app_is_on = True
    file_name = input("Enter name of the file: ") + ".txt"
    input_messages = []

    with open(file_name, "a") as f:
        while app_is_on:
            choice = input("Enter new line of content: ")

            if choice == "stop":
                f.write("\n".join(input_messages))
                app_is_on = False
            else:
                input_messages.append(choice)


if __name__ == "__main__":
    main()
