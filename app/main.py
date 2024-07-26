def main() -> None:
    file_name = input("Enter name of the file: ")
    line = ""
    lines = []
    while line != "stop":
        line = input("Enter new line of content: ")
        if line != "stop":
            lines.append(line)

    with open(f"{file_name}.txt", "w") as f:
        f.writelines(line + "\n" for line in lines)


if __name__ == "__main__":
    main()
