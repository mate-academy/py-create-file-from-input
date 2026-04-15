def main() -> None:
    file_name = input("Enter name of the file: ")
    content = ""
    while True:
        new_content = input("Enter new line of content: ")
        if new_content == "stop":
            break
        content += f"{new_content}\n"
    with open(f"{file_name}.txt", "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
