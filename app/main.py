def main() -> None:
    my_file = open(input("Enter name of the file: ") + ".txt", "w")
    text = input("Enter new line of content: ")
    while text != "stop":
        my_file.write(text + "\n")
        text = input("Enter new line of content: ")
    my_file.close()


if __name__ == "__main__":
    main()
