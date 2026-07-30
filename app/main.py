def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "a") as f:
        line = ""
        while line != "stop":
            line = input("Enter new line of content: ")
            if line != "stop":
                f.write(line + "\n")


if __name__ == "__main__":
    main()
