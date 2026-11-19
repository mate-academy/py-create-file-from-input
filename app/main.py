def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = ""
    while True:
        line_content = input("Enter new line of content: ")
        if line_content == "stop":
            break
        file_content += line_content + "\n"
    with open(file_name + ".txt", "w") as f:
        f.write(file_content)


if __name__ == "__main__":
    main()
