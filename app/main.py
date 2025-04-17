def main() -> None:

    filename = input("Enter name of the file: ")

    lines = []
    line = ""

    while line != "stop":
        line = input("Enter new line of content: ")
        lines.append(line)

    lines.remove("stop")

    with open(f"{filename}.txt", "w") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
