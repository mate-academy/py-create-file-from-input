def main() -> None:
    name = input("Enter name of the file: ")
    file_1 = open(f"{name}.txt", "w+")
    text = None
    context = ""
    while text != "stop":
        text = input("Enter new line of content: ")
        if text != "stop":
            context += text + "\n"
    file_1.write(context)
    print(f"File name: '{name}.txt'")
    print("File content:")
    file_1.seek(0)
    print(file_1.read())


if __name__ == "__main__":
    main()
