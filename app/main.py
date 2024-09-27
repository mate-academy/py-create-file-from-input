def main():
    file_name = input("Enter name of the file: ") + ".txt"
    lines = []
    line = input("Enter new line of content: ")
    while line != 'stop':
        lines.append(line)
        line = input("Enter new line of content: ")
    with open(file_name, 'w') as f:
        for line in lines:
            f.write(line + '\n')


if __name__ == "__main__":
    main()
