def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w"):
        pass
    new_line = ""
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        with open(f"{file_name}.txt", "a") as f:
            f.write(new_line)
            f.write("\n")


if __name__ == "__main__":
    main()
