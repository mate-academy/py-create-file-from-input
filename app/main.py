def main() -> None:
    result = input("Enter name of the file: ") + ".txt"
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(result, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
