def main():
    filename = input("Enter name of the file: ") + ".txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line + "\n")
    with open(filename, "w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    main()
