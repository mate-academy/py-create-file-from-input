def main() -> None:
    file_name = input("Enter name of the file: ")
    file_text = []
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        file_text.append(user_input)
    with open(f"{file_name}.txt", "w") as file:
        file.write("\n".join(file_text))


if __name__ == "__main__":
    main()
