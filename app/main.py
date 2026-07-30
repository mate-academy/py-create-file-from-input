def main() -> None:
    contents_for_user = ""
    file_name = input("Enter name of the file: ")

    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        if contents_for_user:
            contents_for_user += "\n"
        contents_for_user += content

    with open((file_name + ".txt"), "w") as file:
        file.write(contents_for_user)


if __name__ == "__main__":
    main()
