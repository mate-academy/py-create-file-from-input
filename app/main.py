def main() -> None:
    name_of_file = str(input("Enter name of the file: "))
    content = []
    while True:
        text = str(input("Enter new line of content: "))
        if text == "stop":
            break
        content.append(text)

    content_str = "\n".join(content)
    name_of_file += ".txt"
    with open(name_of_file, "w") as file:
        file.write(content_str)

    print(f"File name: {name_of_file}")
    print("File content:")
    print(content_str)


if __name__ == "__main__":
    main()
