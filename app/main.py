def main() -> None:
    name = input("Enter name of the file: ")
    line = input("Enter new line of content: ")
    with open(name + ".txt", "a") as my_file:
        while line != "stop":
            my_file.write(line + "\n")
            line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
