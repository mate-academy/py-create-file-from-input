def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    write_to_file(file_name)


def write_to_file(file_name: str) -> None:
    line = ""
    with open(file_name, "a") as f:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                return

            f.write(line + "\n")


if __name__ == "__main__":
    main()
