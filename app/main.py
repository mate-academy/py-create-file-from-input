def main() -> None:
    name = input("Enter name of the file: ")
    open(name + ".txt", "w")
    with open(name + ".txt", "a") as f:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                f.close()
                return
            f.write(line + "\n")


if __name__ == "__main__":
    main()
