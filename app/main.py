def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []

    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        content.append(user_input)

    with open(f"{file_name}.txt", "w") as file:
        file.write(f"{'\n'.join(content)}")


if __name__ == "__main__":
    main()
