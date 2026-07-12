def main() -> None:
    file_base = input("Enter name of the file: ")
    filename = f"{file_base}.txt"
    open(filename, "a").close()

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        with open(filename, "a") as file:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
