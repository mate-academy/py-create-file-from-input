def main() -> None:
    buffer = ""
    name = input("Enter name of the file: ")
    if name:
        while True:
            nextline = input("Enter new line of content: ")
            if nextline == "stop":
                break
            buffer += nextline + "\n"
    with open(f"{name}.txt", "w") as file:
        file.write(buffer)


if __name__ == "__main__":
    main()
