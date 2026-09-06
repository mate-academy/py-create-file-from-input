def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    file_lines = []
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        elif user_input != "stop":
            file_lines.append(user_input)
    with open(file_name, "w") as file:
        file.write("\n".join(file_lines))


if __name__ == "__main__":
    main()
