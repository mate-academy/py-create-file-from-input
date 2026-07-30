def main() -> None:
    start = input("Enter name of the file: ")
    new_file = open(start + ".txt", "a")
    lines = input("Enter new line of content: ")
    while lines.lower() != "stop":
        new_file.write(lines + "\n")
        lines = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
