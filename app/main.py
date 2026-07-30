def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(f"{file_name}.txt", "w") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
