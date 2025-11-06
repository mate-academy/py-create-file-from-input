def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        lines.append(content)

    with open(f"{file_name}.txt", "w") as file:
        text = "\n".join(lines)
        file.write(text)


if __name__ == "__main__":
    main()
