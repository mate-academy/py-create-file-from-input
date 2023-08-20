def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    content = ""
    while True:
        new_line = input("Enter new line of content: ")
        if new_line != "stop":
            content += new_line + "\n"
        else:
            break
    with open(file_name, "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
