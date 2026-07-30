def main() -> None:
    name = input("Enter name of the file: ")
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)
    with open(f"{name}.txt", "w") as file:
        file.write("\n".join(content))
    pass


if __name__ == "__main__":
    main()
