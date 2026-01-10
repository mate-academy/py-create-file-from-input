def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    with open(filename, "w") as file:
        text = input("Enter new line of content: ")
        while text != "stop":
            file.write(text)
            text = input("Enter new line of content: ")
            if text != "stop":
                file.write("\n")


if __name__ == "__main__":
    main()
