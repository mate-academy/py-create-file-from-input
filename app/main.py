def main() -> None:
    content = []
    file_name = input("Enter name of the file: ") + ".txt"
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)
    with open(file_name, "w") as f:
        for lin in content:
            f.write(f"{lin}\n")


if __name__ == "__main__":
    main()
