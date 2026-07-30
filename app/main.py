def main() -> None:
    text_lines = []
    inp = ""
    counter = 0
    while inp != "stop":
        if counter == 0:
            inp = input("Enter name of the file: ")
            text_lines.append(inp)
            counter += 1
        elif counter >= 1:
            inp = input("Enter new line of content: ")
            if inp != "stop":
                text_lines.append(inp)
    with open(f"{text_lines[0]}.txt", "w") as f:
        for i in range(1, len(text_lines)):
            f.write(text_lines[i] + "\n")


if __name__ == "__main__":
    main()
