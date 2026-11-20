def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)
    pass
    with open(file_name + ".txt", "w") as f:
        for line in lines:
            f.write(line)
            f.write("\n")


if __name__ == "__main__":
    main()
