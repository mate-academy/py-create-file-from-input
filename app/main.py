def main() -> None:
    filename = input("Enter name of the file: ")
    user_content = []
    while True:
        user_line = input("Enter new line of content: ")
        if user_line == "stop":
            break
        user_content.append(user_line + "\n")
    with open(f"{filename}.txt", "w") as file:
        file.writelines(user_content)


if __name__ == "__main__":
    main()
