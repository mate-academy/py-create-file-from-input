def main() -> None:
    file_name = input("Enter name of the file: ")

    lines = []

    while True:
        content = input("Enter new line of content: ")

        if content == "stop":
            break

        else:
            lines.append(content)

    with open(file_name + ".txt", mode="w", encoding="utf-8") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
