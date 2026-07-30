def main() -> None:
    name_of_file = str(input("Enter name of the file: "))
    with open(name_of_file + ".txt", "a") as f:
        while True:
            line = input("Enter new line of content: ")
            if line != "stop":
                f.write(line + "\n")
            else:
                break


if __name__ == "__main__":
    main()
