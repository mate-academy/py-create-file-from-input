def main() -> None:
    name = input("Enter name of the file: ")
    lines = []
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        lines.append(text)

    with open(f"{name}.txt", "a") as f:
        for line in lines:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
