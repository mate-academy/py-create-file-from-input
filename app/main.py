def main() -> None:
    name = input("Enter name of the file: ")
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(name, "w") as f:
        for lin in lines:
            f.write(f"{lin}\n")


if __name__ == "__main__":
    main()
