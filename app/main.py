def main() -> None:
    file_name = str(input("Enter name of the file: ")) + ".txt"
    content = ""
    while True:
        line = str(input("Enter new line of content: "))
        if line.lower() == "stop":
            break
        content += line + "\n"

    with open(file_name, "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
