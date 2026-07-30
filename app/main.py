def main() -> None:
    filename = str(input("Enter name of the file: "))
    if filename[-4:] != ".txt":
        filename += ".txt"
    with open(filename, "w") as file:
        line = ""
        while True:
            line = str(input("Enter new line of content: "))
            if line == "stop":
                break
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
