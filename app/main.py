def main() -> None:
    file_name: str = input("Enter name of the file: ")
    user_file: str = file_name + ".txt"

    content: list = []

    while True:
        user_content: str = input("Enter new line of content: ")
        if user_content == "stop":
            break
        content.append(user_content)

    with open(user_file, "w") as f:
        f.write("\n".join(content))


if __name__ == "__main__":
    main()
