def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "w"):
        pass

    while True:
        content = input("Enter new line of content: ")
        if content.lower() == "stop":
            break
        with open(f"{file_name}.txt", "a") as file:
            file.write(content + "\n")


if __name__ == "__main__":
    main()
