def main() -> None:

    name = input("Enter name of the file: ")

    words = ""
    while True:
        word = input("Enter new line of content: ")
        if word.lower() == "stop":
            break
        words += word + "\n"

    with open(f"{name}.txt", "w") as f:
        f.write(words)


if __name__ == "__main__":
    main()
