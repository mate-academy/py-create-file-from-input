def main() -> None:
    file_name = input("Enter name of the file: ")
    data = []
    while True:
        input_content = input("Enter new line of content: ")
        if input_content == "stop":
            break

        data.append(input_content)

    with open(f"{file_name}.txt", "w") as text_file:
        for item in data:
            text_file.write(item + "\n")


if __name__ == "__main__":
    main()
