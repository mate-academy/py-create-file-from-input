def main() -> None:
    file_name = input("Enter name of the file:").strip()
    with open(file_name, "a") as f:
        new_line = input("Enter new line of content:").strip()
        f.write(new_line)
        while new_line != "stop":
            f.write("\n" + new_line)
            new_line = input("Enter new line of content:").strip()


if __name__ == "__main__":
    main()
