def main() -> None:
    lines = []
    file_name = input("Enter name of the file: ")
    temp = ""
    while temp != "stop":
        temp = input("Enter new line of content: ")
        lines.append(temp)
    file_name += ".txt"

    with open(file_name, "a") as f:
        for line in lines:
            if line == "stop":
                break
            f.write(line)
            f.write("\n")


if __name__ == "__main__":
    main()
