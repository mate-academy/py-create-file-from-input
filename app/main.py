def main():
    file_name = input("Enter name of the file: ")
    text = ""
    while True:
        user_command = input("Enter new line of content: ")
        if user_command == "stop":
            break
        text += user_command + "\n"

    with open(file_name + ".txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
