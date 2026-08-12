def main() -> None:
    name = input("Enter name of the file: ")
    lines: list[str] = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)
    with open(f"{name}.txt", "w") as f:
        if lines:
            f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
