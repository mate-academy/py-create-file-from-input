def main() -> None:
    name = input("Enter name of the file: ")

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    content = "\n".join(lines)

    with open(f"{name}.txt", "w") as f:
        f.write(content)

    print(f"{name}.txt")


if __name__ == "__main__":
    main()
