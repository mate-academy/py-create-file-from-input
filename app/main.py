def main() -> None:
    name = input("Enter name of the file: ")
    filee = open(f"{name}.txt", "w")

    while True:
        newline = input("Enter new line of content: ")
        if newline == "stop":
            filee.close()
            break
        filee.write(f"{newline}\n")


if __name__ == "__main__":
    main()
