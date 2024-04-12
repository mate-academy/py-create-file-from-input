def main() -> None:
    user_input_name = input("Enter name of the file: ")

    content = []

    while 1:
        user_input_line = input("Enter new line of content: ")
        if user_input_line == "stop".lower():
            break
        content.append(user_input_line)

    with open(f"{user_input_name}.txt", "a") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
