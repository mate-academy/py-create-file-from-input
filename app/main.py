def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    while True:
        user_input = input("Enter new line of content: ")

        if user_input == "stop":
            break

        lines.append(user_input)

    with open(file_name + ".txt", "w") as text:
        for line in lines:
            text.write(line + "\n")


if __name__ == "__main__":
    main()
