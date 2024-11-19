def main() -> None:
    name1 = input("Enter name of the file: ") + ".txt"
    new_file = open(name1, "a")
    new_line = input("Enter new line of content: ")

    while new_line != "stop":
        new_file.write(f"{new_line}\n")
        new_line = input("Enter new line of content: ")
    else:
        new_file.close()
        pass


if __name__ == "__main__":
    main()
