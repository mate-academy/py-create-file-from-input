def main() -> None:
    name_of_file = input("Enter name of the file: ") + ".txt"
    with open(f"{name_of_file}", "a") as f:
        while True:
            next_line = input("Enter new line of content: ")
            if next_line == "stop":
                break
            f.write(f"{next_line}\n")


if __name__ == "__main__":
    main()
