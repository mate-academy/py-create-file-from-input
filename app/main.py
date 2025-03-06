def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    flag = True
    while flag:
        user_content = input("Enter new line of content: ")
        if user_content == "stop":
            flag = False
        else:
            content.append(user_content)
    with open(f"{file_name}.txt", "w") as f:
        for i in content:
            f.write(i + "\n")


if __name__ == "__main__":
    main()
