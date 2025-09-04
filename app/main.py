def main() -> None:
    file_name = (input("Enter name of the file: ")
                 .strip() + ".txt")
    file_content = []
    while True:
        entered_content = input("Enter new line of content: ")
        if entered_content.lower() == "stop":
            break
        file_content.append(entered_content)
    with open(file_name, "w") as file:
        file.write("\n".join(file_content))


if __name__ == "__main__":
    main()
