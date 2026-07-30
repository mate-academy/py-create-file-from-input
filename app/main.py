def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "a") as file:
        call_to_action_text = "Enter new line of content: "
        user_text = input(call_to_action_text)

        while user_text != "stop":
            file.write(f"{user_text}\n")
            user_text = input(call_to_action_text)


if __name__ == "__main__":
    main()
