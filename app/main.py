def main() -> None:
    name = input("Enter name of the file: ")
    content_list = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        content_list.append(content + "\n")

    with open(f"{name}.txt", "w") as f:
        f.writelines(content_list)


if __name__ == "__main__":
    main()
