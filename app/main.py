def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    lines = []
    while True:
        line_of_file = input("Enter new line of content: ")
        if line_of_file == "stop":
            break
        lines.append(line_of_file)

    with open(file_name, "w") as f:
        for line in lines:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
