def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    file_content = []

    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        file_content.append(content)

    with open(file_name, "a") as f:
        for line in file_content:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
