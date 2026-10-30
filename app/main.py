def main() -> None:
    title = input("Enter name of the file: ") + ".txt"
    with open(title, "w") as file:
        line = input("Enter new line of content: ")
        while line != "stop":
            file.write(f"{line}\n")
            line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
