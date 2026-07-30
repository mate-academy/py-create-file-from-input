def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    print("Enter new line of content: ")
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(file_name, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
