def main() -> None:
    filename = input("Enter name of the file: ")
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            with open(filename + ".txt", "w") as f:
                f.writelines(lines)
            break
        lines.append(line + "\n")


if __name__ == "__main__":
    main()
