def main() -> None:
    name_file = input("Enter name of the file: ")
    name_file += ".txt"

    with open(name_file, "w") as f:
        while True:
            new_line = input("Enter new line of content: ")

            if new_line.lower() == "stop":
                break

            f.write(new_line + "\n")
    with open(name_file, "r") as f1:
        print(f1.read())


if __name__ == "__main__":
    main()
