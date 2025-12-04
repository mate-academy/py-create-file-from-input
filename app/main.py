def main() -> None:
    file_name = input("Enter name of the file: ")
    full_name = file_name + ".txt"

    lines = []
    while True:
        user_input = input("Enter new line of content: ")
        if user_input.lower() == "stop":
            break
        lines.append(user_input)
    with open(full_name, "w") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
