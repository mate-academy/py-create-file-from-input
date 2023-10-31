def main() -> None:
    name = input("Enter name of the file: ")

    file_name = f"{name}.txt"

    with open(file_name, "w") as f:
        while True:
            next_line = input("Enter new line of content: ")
            if next_line == "stop":
                break
            f.write(f"{next_line}\n")


if __name__ == "__main__":
    main()
