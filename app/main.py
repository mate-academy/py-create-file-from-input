def main() -> None:
    name = input("Enter name of the file: ")
    name += ".txt"
    open(name, "w").close()
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        with open(name, "a") as file:
            file.write(new_line + "\n")


if __name__ == "__main__":
    main()
