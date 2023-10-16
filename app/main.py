def main() -> None:
    file_name = input("Enter name of the file: ")

    content = []
    while True:
        response = input("Enter new line of content: ")
        if response == "stop":
            break
        content.append(f"{response}\n")

    with open(f"{file_name}.txt", "w") as file:
        file.writelines(content)


if __name__ == "__main__":
    main()
