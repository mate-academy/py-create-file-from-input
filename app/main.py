def main():
    file_name = input("Enter name of the file: ") + ".txt"
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line + "\n")

    file = open(file_name, "w")
    file.writelines(lines)


if __name__ == "__main__":
    main()
