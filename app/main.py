def main() -> None:
    # write your code here
    file_name = input("Enter name of the file: ") + ".txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)
    result = "\n".join(lines)
    with open(file_name, "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
