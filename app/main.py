def main() -> None:
    filename = input("Enter name of the file: ")
    content = []

    line = input("Enter new line of content: ")
    while line != "stop":
        content.append(line)
        line = input("Enter new line of content: ")

    with open(f"{filename}.txt", "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
