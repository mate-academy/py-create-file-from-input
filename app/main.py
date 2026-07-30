def main():
    name_of_file = input("Enter name of the file: ")
    list_of_line = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        list_of_line.append(line)

    with open(name_of_file + ".txt", "a") as f:
        for line in list_of_line:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
