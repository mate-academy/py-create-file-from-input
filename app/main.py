def main() -> None:
    name = input("Enter name of the file: ")

    while True:
        content = input("Enter new line of content: ")
        content_list = []
        if content == "stop":
            with open(f"{name}.txt", "a") as file:
                file.writelines(content_list)
                break

        content_list.append(f"{content}\n")

        with open(f"{name}.txt", "a") as file:
            file.writelines(content_list)


if __name__ == "__main__":
    main()
