def main() -> None:
    file_name = input("Enter file name: ")
    file_text = ""
    while True:
        user_text = input("Enter a text to save it to file: ")

        if user_text == "stop":
            break

        file_text += f"{user_text}\n"

    with open(file_name, "w") as file:
        file.write(file_text)


if __name__ == "__main__":
    main()
