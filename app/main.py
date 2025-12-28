def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []

    while True:
        content = input("Enter new line of content: ")

        if content == "stop":
            break

        file_content.append(content)

    with open(f"{file_name}.txt", "w") as file:
        file.write("\n".join(file_content))


if __name__ == "__main__":
    main()
