def main() -> (None, str):
    file_content = []
    name = input("Enter name of the file: ").strip()

    if not name:
        print("File name cannot be empty!")
        return

    if not name.endswith(".txt"):
        name += ".txt"

    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        file_content.append(content)

    with open(f"{name}", "w") as file:
        for item in file_content:
            file.write(item + "\n")


if __name__ == "__main__":
    main()
