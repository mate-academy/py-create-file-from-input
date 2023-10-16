def main() -> None:
    file_name = input("Enter name of the file: ")

    lines = ""
    while True:
        line = input("Enter new line of content: ")
        if line != "stop":
            lines += line + "\n"
        else:
            break

    with open(file_name + ".txt", "w") as f:
        f.write(lines)


if __name__ == "__main__":
    main()
