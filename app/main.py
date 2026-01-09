def main() -> None:
    filename = input("Enter name of the file: ")
    outfile = open(filename + ".txt", "a")
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            outfile.write(line)
    outfile.close()


if __name__ == "__main__":
    main()
