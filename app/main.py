def main() -> None:
    filename = input("Enter name of the file: ")
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(f"{filename}.txt", "w") as file:
        for line in lines:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
