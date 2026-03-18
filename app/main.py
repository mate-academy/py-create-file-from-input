def main() -> None:
    name = input("Enter name of the file: ")
    content = []

    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        content.append(text)

    file_name = name + ".txt"
    print(f'File name: "{file_name}"')
    print("File content:")
    with open(file_name, "a") as f:
        for text in content:
            print(text)
            f.write(f"{text}\n")


if __name__ == "__main__":
    main()
