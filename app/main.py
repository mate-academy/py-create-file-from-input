def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    app = open(name, "a")
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        else:
            app.write(text)
            app.write("\n")


if __name__ == "__main__":
    main()
