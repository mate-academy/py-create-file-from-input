def main() -> None:
    name = input("Enter name of the file: ")
    filename = f"{name}.txt"

    file1 = open(filename, "w")

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        file1.write(f"{line}\n")

    file1.close()


if __name__ == "__main__":
    main()
