def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    with open(filename, "a") as f:
        while True:
            line = input("Enter new line of content: ")
            if line != "stop":
                f.write(line + "\n")
            else:
                break


if __name__ == "__main__":
    main()
