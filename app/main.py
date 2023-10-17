def main() -> None:
    filename = input("Enter name of the file: ")
    line = None
    lines = []
    while line != "stop":
        if line:
            lines.append(line)
        line = input("Enter new line of content: ")
    with open(f"{filename}.txt", "w") as file:
        file.write("\n".join(line for line in lines))


if __name__ == "__main__":
    main()
