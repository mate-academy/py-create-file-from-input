def main() -> None:
    name = str(input("Enter name of the file: "))
    text = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        text.append(line)

    with open(f"{name}.txt", "w") as file:
        file.write("\n".join(text))


if __name__ == "__main__":
    main()
