def main() -> None:
    file_name = input("Enter name of the file: ")
    filename = f"{file_name}.txt"
    with open(filename, "w") as file:
        pass
    while True:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        with open(filename, "a") as file:
            file.write(new_line + "\n")


if __name__ == "__main__":
    main()
