def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)
    with open(file_name, "a") as file_append:
        for line in lines:
            file_append.write(f"{line}\n")


if __name__ == "__main__":
    main()
