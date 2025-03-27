def main() -> None:
    file_name = f"{input("Enter name of the file: ")}.txt"

    with open(file_name, "a") as f:
        while True:
            write_line = f"{input("Enter new line of content: ")}\n"
            if str(write_line.lower().strip()) == "stop":
                break
            f.write(write_line)


if __name__ == "__main__":
    main()
