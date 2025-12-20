def main():
    file_basename = input("Enter name of the file: ")
    filename = file_basename + ".txt"

    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    file = open(filename, "w")
    file.write("\n".join(lines))
    file.close()


if __name__ == "__main__":
    main()
