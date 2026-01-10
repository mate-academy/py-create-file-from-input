def main() -> None:
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    with open(file_name, "a") as file:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            file.write(content + "\n")


if __name__ == "__main__":
    main()
