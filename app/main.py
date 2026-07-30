def main() -> None:
    file_name = str(input("Enter name of the file: ")) + ".txt"
    content_list = []
    content = str(input("Enter new line of content: "))
    while content != "stop":
        content_list.append(content)
        content = str(input("Enter new line of content: "))

    with open(file_name, "w") as file:
        file.write("\n".join(content_list))
    # with open(file_name, "a") as file:
    #     content = str(input("Enter new line of content: "))
    #     file.write(content + "\n")
    #     while content != "stop":
    #         content = str(input("Enter new line of content: "))
    #         file.write(content + "\n")


if __name__ == "__main__":
    main()
