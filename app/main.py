def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = ""
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content += f"{line}\n"
    with open(file_name, "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
