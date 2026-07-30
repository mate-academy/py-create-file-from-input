def main() -> None:
    file_name: str = input("Enter name of the file: ") + ".txt"

    content: list[str] = []
    print("Enter new line of content. Type 'stop' to finish.")

    while True:
        line: str = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(file_name, "w", encoding="utf-8") as file:
        for line in content:
            file.write(line + "\n")

    print(f"File '{file_name}' has been created and filled with content.")


if __name__ == "__main__":
    main()
