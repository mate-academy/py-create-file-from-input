def main() -> None:
    file_name = input("Enter name of the file: ")
    text = None
    content = []
    while text != "stop":
        text = input("Enter new line of content: ")
        if text != "stop":
            content.append(text)
    with open(f"{file_name}.txt", "w") as f:
        f.write("\n".join(content))


if __name__ == "__main__":
    main()
