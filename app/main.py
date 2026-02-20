def main() -> None:
    name = input("Enter name of the file: ").strip()
    name += ".txt"

    lines = []

    while True:
        inp = input("Enter new line of content: ")
        if inp.lower() == "stop":
            break
        lines.append(inp)

    with open(name, "w") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
