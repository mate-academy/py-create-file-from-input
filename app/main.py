def main() -> None:
    lines = list()
    name_file = input("Enter name of the file: ")
    name_file_txt = name_file + ".txt"
    while True:
        line_name = input("Enter new line of content: ")
        if line_name == "stop":
            break
        lines.append(line_name)
    with open(name_file_txt, "w") as f:
        for i in lines:
            f.write(i + "\n")


if __name__ == "__main__":
    main()
