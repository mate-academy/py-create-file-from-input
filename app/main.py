def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    while True:
        input_messages = input("Enter new line of content: ")
        if input_messages.lower() == "stop":
            break
        lines.append(input_messages)

    with open(f"{file_name}.txt", "a") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
