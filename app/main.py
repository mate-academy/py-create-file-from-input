def main() -> None:
    file_name = input("Enter name of the file: ")
    text = []
    while True:
        sentence = input("Enter new line of content: ")
        if sentence.lower() == "stop":
            break
        text.append(sentence)
    text = "\n".join(text)
    output_file = open(file_name + ".txt", "w")
    output_file.write(text)


if __name__ == "__main__":
    main()
