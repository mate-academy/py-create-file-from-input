def main() -> None:
    name_file = input("Enter name of the file: ")
    while True:
        with open(f"{name_file}.txt", "a") as f:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            f.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
