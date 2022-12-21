def main() -> None:
    name_file = input("Enter name of the file: ") + ".txt"
    with open(name_file, "a") as file:
        while True:
            some = input("Enter new line of content: ")
            if some == "stop":
                break
            file.write(some + "\n")


if __name__ == "__main__":
    main()
