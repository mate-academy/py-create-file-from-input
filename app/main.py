STOP_COMMAND = "stop"


def main() -> None:
    file_content: list[str] = []
    file_name: str = input("Enter name of the file: ")

    while True:
        content_input: str = input("Enter new line of content: ")

        if content_input == STOP_COMMAND:
            break

        file_content.append(f"{content_input}\n")

    with open(f"{file_name}.txt", "a") as file:
        for line in file_content:
            file.write(line)


if __name__ == "__main__":
    main()
