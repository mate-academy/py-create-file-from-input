def main() -> None:
    file_name = input("Enter name of the file: ")
    user_text = []
    while True:
        user_input = input("Enter new line of content: ")

        if user_input != "stop":
            user_text.append(user_input)
        else:
            break
    with open(f"{file_name}.txt", "w") as f:
        for line in user_text:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
