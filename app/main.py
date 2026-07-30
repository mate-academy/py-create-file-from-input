def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name_txt = file_name + ".txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line + "\n")

    with open(file_name_txt, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
