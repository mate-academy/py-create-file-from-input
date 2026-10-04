def main() -> None:

    file_name = input("Enter name of the file: ") + ".txt"

    lines = []
    if file_name:
        while True:
            file_content = input("Enter new line of content: ")
            if file_content.lower() == "stop":
                break
            lines.append(file_content)

    text = "\n".join(lines)
    with open(file_name, "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
