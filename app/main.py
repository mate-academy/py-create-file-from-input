def main() -> None:
    name = input("Enter name of the file: ")
    filename = str(name) + ".txt"

    open(filename, "w").close()

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        with open(filename, "a") as f:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()