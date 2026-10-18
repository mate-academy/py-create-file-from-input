def main() -> None:
    filename = open(input("Enter name of the file: ") + ".txt", "w")
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        filename.write(line + "\n")
    filename.close()
    return None


if __name__ == "__main__":
    main()
