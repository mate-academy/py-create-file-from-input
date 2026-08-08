def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    with open(filename, "w") as f:
        text_object = input("Enter new line of content: ", )
        while text_object != "stop":
            f.write(text_object + "\n")
            text_object = input("Enter new line of content: ", )


if __name__ == "__main__":
    main()
