def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    new_line = input("Enter new line of content: ")

    with open(file_name, "w") as f:
        if new_line.lower() == "stop":
            pass
        else:
            f.write(f"{new_line}\n")
    while new_line != "stop":
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        with open(file_name, "a") as f:
            f.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
