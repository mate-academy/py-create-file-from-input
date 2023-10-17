def main() -> None:
    filename = input("Enter name of the file: ")
    content = []
    user_content = ""
    while user_content != "stop":
        user_content = input("Enter new line of content: ")
        content.append(user_content)

    with open(filename, "w") as f:
        for text in content:
            f.write(text + "\n")


if __name__ == "__main__":
    main()
