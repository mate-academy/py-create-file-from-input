def main() -> None:

    file_name = input("Enter name of the file: ")
    content = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        content.append(new_line)

    path = file_name + ".txt"

    with open(path, "w") as f:
        f.write("\n".join(content))


if __name__ == "__main__":
    main()
