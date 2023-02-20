def main() -> None:
    filename = input("Enter name of the file: ")

    with open(filename + ".txt", "w") as f:

        while True:
            line = input("Enter new line of content: ")
            if line.lower() == "stop":
                break
            f.write(line + "\n")

    print("File created: " + filename + ".txt")


if __name__ == "__main__":
    main()
