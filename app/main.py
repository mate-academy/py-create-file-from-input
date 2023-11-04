def main() -> None:
    filename = input("Enter name of the file: ")
    with open(filename + ".txt", "a") as f:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            else:
                f.write(line + "\n")


if __name__ == "__main__":
    main()
