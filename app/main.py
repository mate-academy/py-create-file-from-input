def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    line = ""
    with open(filename, "w") as f:
        while line != "stop":
            line = input("Enter new line of content: ")
            if line != "stop":
                f.write(line + "\n")


if __name__ == "__main__":
    main()
