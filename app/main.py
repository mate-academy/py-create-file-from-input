def main() -> None:
    name_file = input("Enter name of the file: ") + ".txt"
    text = ""
    fille = open(name_file, "a")
    while text != "stop":
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        fille.write(text + "\n")


if __name__ == "__main__":
    main()
