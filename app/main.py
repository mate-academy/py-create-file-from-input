def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    content = ""

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content += line + "\n"

    with open(file_name, "w") as file:
        file.write(content)
    print(f"File '{file_name}' created successfully!")


if __name__ == "__main__":
    main()
