def main() -> None:
    name = input("Enter name of the file: ")
    with open(name + ".txt", "a") as file:
        line = input("Enter new line of content: ")
        while line != "stop":
            file.write(f"{line}\n")
            line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
