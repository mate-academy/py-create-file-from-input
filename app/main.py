def main() -> None:
    filename = input("Enter name of the file: ")
    if not filename.endswith(".txt"):
        filename += ".txt"

    content = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    # Записуємо вміст у файл
    with open(filename, 'w') as file:
        file.write('\n'.join(content))

    # Читаємо файл і шукаємо слова на w/W
    w_words = []
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()

        for word in words:
            if word.lower().startswith('w'):
                w_words.append(word.lower())

    w_words.sort()
    print(w_words)


if __name__ == "__main__":
    main()
