def main() -> None:
    with open(str(input("Enter name of the file: ")) + ".txt", "w") as f:
        line_in_file = str(input("Enter new line of content: "))
        while line_in_file != "stop":
            f.write(line_in_file + "\n")
            line_in_file = str(input("Enter new line of content: "))


if __name__ == "__main__":
    main()
