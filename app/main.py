def main() -> None:
    name = input("Enter name of the file: ")
    file_content = ""
    file_content_list = []
    while file_content != "stop":
        file_content = input("Enter new line of content: ")
        file_content_list.append(file_content)

    with open(f"{name}.txt", "w") as f:
        for line in file_content_list[: -1]:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
