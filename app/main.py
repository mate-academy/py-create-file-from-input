def main() -> None:
    filename = input("Enter name of the file: ")

    if not filename.endswith(".txt"):
        filename = filename + ".txt"

    with open(filename, "a") as f:
        text = ""
        while text != "stop":
            text = input("Enter new line of content: ")
            if text != "stop":
                f.write(text + "\n")


if __name__ == "__main__":
    main()
