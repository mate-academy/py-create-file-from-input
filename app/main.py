def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    result = []
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        result.append(user_input)

    with open(file_name, "w") as file:
        result_text = "\n".join(result)
        file.write(result_text)


if __name__ == "__main__":
    main()
