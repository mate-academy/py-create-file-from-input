def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    list_of_words = []
    while True:
        data = input("Enter new line of content: ")
        if data == "stop":
            break
        list_of_words.append(data + "\n")

    with open(name, "a") as f:
        for word in list_of_words:
            f.write(word)


if __name__ == "__main__":
    main()
