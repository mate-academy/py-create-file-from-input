def main():
    name_of_file = input("Enter name of the file: ")
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line + "\n")

    with open(name_of_file + ".txt", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
