def main() -> None:
    file_name = input("Enter name of the file: ")
    content_list = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        content_list.append(f"{content}\n")
    with open(f"{file_name}.txt", "a") as my_file:
        my_file.writelines(content_list)


if __name__ == "__main__":
    main()
