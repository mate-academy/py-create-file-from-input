def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    line = input("Enter new line of content: ")
    while line != "stop":
        lines.append(line)
        line = input("Enter new line of content: ")
    with open(file_name + ".txt", "w") as f:
        for item in lines:
            f.write(item + "\n")


if __name__ == "__main__":
    main()
