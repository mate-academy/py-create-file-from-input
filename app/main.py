def main() -> None:
    # write your code here
    name = input("Enter name of the file: ")
    content_list = []

    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        content_list.append(f"{content}\n")

    with open(f"{name}.txt", "w+") as file:
        for con in content_list:
            file.write(con)


if __name__ == "__main__":
    main()
