def main() -> None:
    file_name = (input("Enter name of the file: ") + ".txt")
    text = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        text.append(line)
    with open(file_name, "w") as f:
        for line in text:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
