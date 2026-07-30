def main() -> None:
    content = ""
    file_name = input("Enter name of the file: ")
    full_name = file_name + ".txt"
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        content += new_line + "\n"
    with open(full_name, "a") as f:
        f.write(content)


if __name__ == "__main__":
    main()
