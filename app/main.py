def main() -> None:
    filename = input("Enter name of the file: ")
    with open(filename + ".txt", "w") as f:
        while True:
            inp = input("Enter new line of content: ")
            if inp == "stop":
                break
            else:
                f.write(inp + "\n")


if __name__ == "__main__":
    main()
