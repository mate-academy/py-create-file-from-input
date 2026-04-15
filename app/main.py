def main() -> None:
    with open(input("Enter name of the file: ") + ".txt", "w") as f:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            f.write(line + "\n")
    pass


if __name__ == "__main__":
    main()
