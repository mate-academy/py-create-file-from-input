def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as f:
        new_line = input("Enter new line of content: ")
        while new_line != "stop":
            f.write(f"{new_line}\n")
            new_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
