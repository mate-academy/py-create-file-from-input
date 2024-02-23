def main() -> None:
    filename = input("Enter name of the file: ")
    with open(filename + ".txt", "w") as file:
        line = input("Enter new line of content: ")
        while line != "stop":
            file.write(line + "\n")
            line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
