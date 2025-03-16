def main() -> None:
    file_name = str(input("Enter name of the file: ")) + ".txt"
    all_content = []

    while True:

        content = input("Enter new line of content: ")

        if content.lower() == "stop":
            break
        all_content.append(content)

    with open(file_name, "a") as file:
        if all_content:
            file.write("\n".join(all_content) + "\n")
        file.write("")


if __name__ == "__main__":
    main()
