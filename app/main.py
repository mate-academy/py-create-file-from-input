def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "a") as f:
        line = input("Enter new line of content: ")
        while line != "stop":
            f.write(line + "\n")
            line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
