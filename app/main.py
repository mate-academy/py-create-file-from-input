def main() -> None:
    name_of_file = input("Enter name of the file: ")
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)
    with open(f"{name_of_file}.txt", "w") as f:
        for line in lines:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
