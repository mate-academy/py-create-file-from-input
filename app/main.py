def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = file_name + ".txt"
    content = []

    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        content.append(user_input)

    with open(file_name, mode="w") as f:
        f.write("\n".join(content))


if __name__ == "__main__":
    main()
