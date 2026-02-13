def main() -> None:
    name = input("Enter name of the file: ")
    file_user = open(f"{name}.txt", "a")
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        file_user.write(content + "\n")
    file_user.close()


if __name__ == "__main__":
    main()
