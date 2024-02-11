def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    with open(name, "w") as f:
        while True:
            newline = input("Enter new line of content: ")
            if newline == "stop":
                break
            f.write(newline + "\n")


if __name__ == "__main__":
    main()
