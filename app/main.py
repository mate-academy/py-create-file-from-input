def main() -> None:
    name_input = input("Enter name of the file: ")

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    full_filename = f"{name_input}.txt"
    with open(full_filename, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
