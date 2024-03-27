def main() -> None:
    name = input("Enter name of the file: ")
    with open(name, "a") as f:
        while 1:
            info = input("Enter new line of content: ")
            if info == "stop":
                break
            f.write(info + "\n")


if __name__ == "__main__":
    main()
