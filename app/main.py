def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    file_content = ""
    while True:
        content = input("Enter new line of content: ") + "\n"
        if content == "stop\n":
            break
        file_content += content

    with open(file_name, "w") as file:
        file.write(file_content)


if __name__ == "__main__":
    main()
