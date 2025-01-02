def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    lines = []
    while True:
        file_content = input("Enter new line of content: ")
        if file_content == "stop":
            break
        lines.append(file_content)
    with open(file_name, "a") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
