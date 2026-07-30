def main() -> None:
    file_name = input("Enter name of the file: ")
    lines_list = []
    while True:
        line = input("Enter new line of content: ")
        if line != "stop":
            lines_list.append(line)
        else:
            break
    with open(f"{file_name}.txt", "a") as f:
        for line in lines_list:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
