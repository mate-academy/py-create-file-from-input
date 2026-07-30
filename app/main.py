def main() -> None:
    name_file = input("Enter name of the file: ")
    content_user = ""
    while True:
        input_user = input("Enter new line of content: ")
        if input_user == "stop":
            break
        content_user = content_user + input_user + "\n"
    with open(f"{name_file}.txt", "w") as f:
        f.write(f"{content_user}")


if __name__ == "__main__":
    main()
