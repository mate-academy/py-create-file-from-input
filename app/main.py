def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    with open(name, "w") as file:
        line = input("Enter new line of content: ")
        while line.lower() != "stop":
            file.write(line + "\n")
            line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
