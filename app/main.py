def main():
    name = input("Enter name of the file: ") + ".txt"
    text = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        text.append(new_line)

    with open(name, "w") as file:
        for line in text:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
