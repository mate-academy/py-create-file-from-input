def main() -> None:
    name = input("Enter name of the file: ")
    name = f"{name}.txt"
    with open(name, "a") as file:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            file.write(text + "\n")


if __name__ == "__main__":
    main()
