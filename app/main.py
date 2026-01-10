def main() -> None:

    filename = input("Enter name of the file: ")
    content = []
    while True:
        user_content = input("Enter new line of content: ")
        if user_content == "stop":
            break
        content.append(user_content)

    with open(f"{filename}.txt", "w") as f:
        f.writelines(line + "\n" for line in content)


if __name__ == "__main__":
    main()
