def main() -> None:
    file_name = input("Enter name of the file: ")
    file_contents = ""
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        file_contents += (content + "\n")
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_contents)


if __name__ == "__main__":
    main()
