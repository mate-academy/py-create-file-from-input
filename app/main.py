def main() -> None:
    while True:
        file_name = input("Enter name of the file: ") + ".txt"
        if len(file_name) > 0:
            break

    with open(file_name, "w"):
        pass

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        with open(file_name, "a") as f:
            f.write(new_line + "\n")


if __name__ == "__main__":
    main()
