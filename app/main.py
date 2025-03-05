def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    with open(file_name, "w") as f:
        while True:
            write_line = input("Enter new line of content: ")
            if write_line == "stop":
                break

            f.write(write_line + "\n")


if __name__ == "__main__":
    main()
