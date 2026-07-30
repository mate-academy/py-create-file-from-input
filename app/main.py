def main() -> None:
    name = input("Enter name of the file: ")
    text = []
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        text.append(user_input)
    with open(name + ".txt", "w") as file:
        for line in text:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
