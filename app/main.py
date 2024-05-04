def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = []
    while True:
        next_line = input("Enter new line of content: ") + "\n"
        if next_line != "stop\n":
            content.append(next_line)
        else:
            break
    cur_file = open(file_name, "w")
    for line in content:
        cur_file.write(line)


if __name__ == "__main__":
    main()
