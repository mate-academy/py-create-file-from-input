def main() -> None:
    user_file = input("Enter name of the file: ")
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    file_content = "\n".join(content)

    file_path = f"{user_file}.txt"

    with open(file_path, "w") as f:
        f.write(file_content)


if __name__ == "__main__":
    main()
