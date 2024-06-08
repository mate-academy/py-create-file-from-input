def main() -> None:
    file_name = input("Enter the file name: ") + ".txt"
    new_line = input("Enter next line of the content: ")
    with open(file_name, "a") as f:
        while new_line != "stop":
            f.write(new_line)


if __name__ == "__main__":
    main()
