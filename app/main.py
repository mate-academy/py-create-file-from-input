def main() -> None:
    name_file = input("Enter name of the file: ")

    with open(f"{name_file}.txt", "w") as f:
        line_in_file = input("Enter new line of content: ")

        while line_in_file != "stop":
            f.write(f"{line_in_file}\n")
            line_in_file = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
