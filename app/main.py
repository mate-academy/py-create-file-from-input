def main() -> None:
    name = input("Enter name of the file: ")
    name += ".txt"
    with open(name, "a") as f:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            text += "\n"
            f.write(text)


if __name__ == "__main__":
    main()
