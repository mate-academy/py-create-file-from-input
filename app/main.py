def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    file_content = ""
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        file_content += line + "\n"
    with open(file_name, "w") as file:
        file.write(file_content)


if __name__ == "__main__":
    main()
