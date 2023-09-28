def main() -> None:
    name = input("Enter name of the file: ")
    with open(name + ".txt", "w") as file:
        while True:
            add_text = input("Enter new line of content: ")
            if add_text == "stop":
                break
            file.write(add_text + "\n")


if __name__ == "__main__":
    main()
