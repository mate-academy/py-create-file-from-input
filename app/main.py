def main() -> None:
    file_name = input("Enter name of the file: ")
    user_text = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        user_text.append(new_line)

    with open(file_name + ".txt", "w") as file:
        for i in user_text:
            file.write(f"{i}\n")


if __name__ == "__main__":
    main()
