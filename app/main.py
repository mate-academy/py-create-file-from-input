def main() -> None:
    name = str(input("Enter name of the file: ")) + ".txt"
    content = []
    while True:
        current_line = str(input("Enter new line of content: "))
        if current_line != "stop":
            content.append(current_line)
        else:
            break
    with open(name, "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
