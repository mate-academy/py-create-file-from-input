def main() -> None:
    file_name = input("Enter name of the file: ")

    if not file_name.endswith(".txt"):
        file_name = file_name + ".txt"

    with open(file_name, "w") as f:
        while True:
            next_line = input("Enter new line of content: ")

            if next_line == "stop":
                break
            f.write(f"{next_line}\n")


if __name__ == "__main__":
    main()
