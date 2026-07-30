def main() -> None:
    file_name = input("Enter name of the file: ")
    file_text = ""
    while True:
        user_text = input("Enter new line of content: ")

        if user_text == "stop":
            break

        file_text += f"{user_text}\n"

    with open(f"{file_name}.txt", "w") as file:
        file.write(file_text)


if __name__ == "__main__":
    main()
