def main() -> None:
    file_name = input("Enter name of the file: ")

    content = ""
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content = content + line + "\n"
    with open(f"{file_name}.txt", "a") as f:
        f.write(content)


if __name__ == "__main__":
    main()
