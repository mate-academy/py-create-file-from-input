def main() -> None:
    file_name = input("Enter name of the file: ")
    command_storage = []
    while True:
        user_command = input("Enter new line of content: ")
        if user_command == "stop":
            break
        command_storage.append(user_command)

    with open(f"{file_name}.txt", "a") as f:
        for command in command_storage:
            f.write(command + "\n")


if __name__ == "__main__":
    main()
