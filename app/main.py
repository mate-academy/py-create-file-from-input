def main() -> None:
    name = input("Enter name of the file: ")
    content = ""
    while True:
        line = input("Enter new line of content: ")
        if line != "stop":
            content += line + "\n"
        else:
            break

    with open(name + ".txt", "w") as f:
        f.write(content.strip())


if __name__ == "__main__":
    main()
