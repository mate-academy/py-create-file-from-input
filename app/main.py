def main() -> None:
    lines = []
    name = input("Enter name of the file: ")
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            lines.append(line)
    with open(f"{name}.txt", "w") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
