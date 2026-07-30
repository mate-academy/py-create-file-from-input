def main() -> None:
    name = input("Enter name of the file: ")
    line = input("Enter new line of content: ")
    with open(f"{name}.txt", "a") as file:
        while line != "stop":
            file.write(line + "\n")
            line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
