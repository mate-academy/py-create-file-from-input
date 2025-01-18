def main() -> None:
    name = input("Enter name of the file: ")
    name = name + ".txt"
    text_file = open(name, "w")
    while True:
        temp = input("Enter new line of content: ")
        if temp == "stop":
            text_file.close()
            break
        text_file.write(temp + "\n")


if __name__ == "__main__":
    main()
