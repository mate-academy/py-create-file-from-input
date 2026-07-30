def main() -> None:
    file_name = input("Enter name of the file: ")
    lines_to_write = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines_to_write.append(line)
    with open(file_name + ".txt", "w") as f:
        f.writelines(f"{line}\n" for line in lines_to_write)


if __name__ == "__main__":
    main()
