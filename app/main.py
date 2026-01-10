def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    file_content = []

    while True:
        user_data = input("Enter new line of content: ")

        if user_data == "stop":
            break

        file_content.append(user_data)

    with open(file_name, "w") as file:
        for item in file_content:
            file.write(item + "\n")


if __name__ == "__main__":
    main()
