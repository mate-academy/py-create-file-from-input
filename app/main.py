def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    with open(filename, "w") as f:
        while True:
            file_write = input("Enter new line of content: ")
            if file_write == "stop":
                break
            f.write(file_write + "\n")


if __name__ == "__main__":
    main()
