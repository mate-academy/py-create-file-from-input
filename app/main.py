def main() -> None:
    file_name = input() + ".txt"
    content = []

    while True:
        line = input()
        if line.lower() == "stop":
            break
        content.append(line)

    with open(file_name, "w", encoding="utf-8") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
