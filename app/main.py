def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    lines = []
    while True:
        text = input("Enter new line of content: ")
        if text.lower() == "stop":
            break
        lines.append(text)
    with open(name, "w") as f:
        for line in lines:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
