def main() -> None:
    filename = str(input("Enter name of the file: ") + ".txt")
    text_to_write = ""
    while True:
        temp = str(input("Enter new line of content: "))
        if temp == "stop":
            break
        text_to_write += temp + "\n"
    with open(filename, "w") as file:
        file.write(text_to_write)


if __name__ == "__main__":
    main()
