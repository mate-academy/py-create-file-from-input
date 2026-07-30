def main() -> None:
    file_name = input("Enter name of the file: ")
    correct_file_name = file_name + ".txt"
    opened_file = open(correct_file_name, "a")
    word = ""
    text = []
    while word != "stop":
        word = input("Enter new line of content: ")
        if word != "stop":
            text.append(word + "\n")
    print(f"File name: {file_name}")
    print("File content:")
    for line in text:
        opened_file.write(line)
        print(line)
    opened_file.close()


if __name__ == "__main__":
    main()
