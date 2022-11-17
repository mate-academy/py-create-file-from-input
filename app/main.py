def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as f:
        while True:
            next_line = input("Enter new line of content: ")
            if next_line == "stop":
                break
            f.write(f"{next_line}\n")


if __name__ == "__main__":
    main()
