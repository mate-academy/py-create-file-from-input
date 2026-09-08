def main() -> None:
    name = input("Enter name of the file: ")
    name = f"{name}.txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            lines.append(line)

    with open(name, "w") as f:
        for line in lines:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
