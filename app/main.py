def main() -> None:
    file_name = input("Enter name of the file: ")
    text = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        text.append(line)
    with open(f"{file_name}.txt", "w") as file:
        for line in text:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
