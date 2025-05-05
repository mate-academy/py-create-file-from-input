def main():
    text = input("Enter name of the file: ")
    text += ".txt"
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(text, 'w') as f:
        for line in lines:
            f.write(line + "\n")

if __name__ == "__main__":
    main()
