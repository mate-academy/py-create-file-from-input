def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line != "stop":
            lines.append(new_line)
        else:
            break
    with open(f"{file_name}.txt", "w") as result:
        for line in lines:
            result.write(line + "\n")


if __name__ == "__main__":
    main()
