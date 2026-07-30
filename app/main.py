def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    file_content = []

    while True:
        content = input("Enter new line of content: ")
        if content.lower() == "stop":
            break
        file_content.append(content)

    with open(file_name, "w") as file:
        file.write("\n".join(file_content))

    print(f"File '{file_name}' has been created with the provided content.")


if __name__ == "__main__":
    main()
