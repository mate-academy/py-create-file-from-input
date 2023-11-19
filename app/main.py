def main() -> None:
    filename = input("Enter name of the file: ")
    filename += ".txt"
    text = ""
    while True:
        input_text = input("Enter new line of content: ")
        if input_text == "stop":
            break
        text += input_text + "\n"

    with open(filename, "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
