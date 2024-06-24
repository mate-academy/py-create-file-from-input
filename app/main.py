def main() -> None:
    name_file = input("Enter name of the file: ")
    user_text = []

    while True:
        text_temp = input("Enter new line of content: ")
        if text_temp == "stop":
            break
        user_text.append(text_temp)

    with open(f"{name_file}.txt", "w") as user_file:
        for line in user_text:
            user_file.write(line + "\n")


if __name__ == "__main__":
    main()
