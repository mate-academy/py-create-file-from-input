def main() -> None:
    filename = input("Enter name of the file: ")
    content = []
    new_line = input("Enter new line of content: ")
    while new_line != "stop":
        content.append(new_line)
        new_line = input("Enter new line of content: ")

    with open(f"{filename}.txt", "a") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
