def main() -> None:
    name = input("Enter name of the file: ")
    strings = ""
    while True:
        curr_line = input("Enter new line of content: ")
        if curr_line == "stop":
            break
        strings += curr_line + "\n"
    with open(name + ".txt", "w") as file:
        file.write(strings)


if __name__ == "__main__":
    main()
