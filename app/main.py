def main() -> None:
    filename = input("Enter name of the file: ")
    lines = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        lines.append(new_line)

    with open(f"{filename}.txt", "w") as f:
        for line in lines:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
