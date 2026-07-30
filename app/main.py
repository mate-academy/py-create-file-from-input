def main() -> None:
    first = input("Enter name of the file: ")
    head = []
    while True:
        other = input("Enter new line of content: ")
        if other == "stop":
            break
        head.append(other)
    file_name = first + ".txt"
    with open(file_name, "w") as file:
        for i in head:
            file.write("{}\n".format(i))


if __name__ == "__main__":
    main()
