def main() -> None:
    name = input("Enter name of the file: ")
    text = []
    while True:
        text_input = input("Enter new line of content: ")
        if text_input == "stop":
            break
        text.append(text_input)

    output_file = open(f"{name}.txt", "w")
    for line in text:
        output_file.write(line + "\n")
    output_file.close()


if __name__ == "__main__":
    main()
