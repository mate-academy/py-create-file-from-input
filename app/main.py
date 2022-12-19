def main() -> None:

    name = input("Enter name of the file: ")
    filex = open(str(name) + ".txt", "a")
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            filex.close()
            break
        filex.write(text + "\n")


if __name__ == "__main__":
    main()
