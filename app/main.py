def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    with open(name, "a") as file:
        while True:
            string = input("Enter new line of content: ") + "\n"
            if string == "stop\n":
                break
            file.write(string)


if __name__ == "__main__":
    main()
