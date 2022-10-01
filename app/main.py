def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []

    while True:
        line_content = input("Enter new line of content: ")
        if line_content == "stop":
            break
        file_content.append(line_content)

    with open(f"{file_name}.txt", "a") as file_record:
        file_record.write("\n".join(file_content))


if __name__ == "__main__":
    main()
