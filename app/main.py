def main() -> None:
    content_list = []
    file_name = input("Enter name of the file: ")

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_list.append(f"{line}\n")

    with open(f"{file_name}.txt", "w") as f:
        f.writelines(content_list)


if __name__ == "__main__":
    main()
