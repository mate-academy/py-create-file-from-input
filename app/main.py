def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    lines = []
    print("Enter new line of content:")
    while True:
        line = input()
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(file_name, "w") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
