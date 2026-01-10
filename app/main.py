def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    text = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        text.append(f"{line}\n")
    with open(filename, "w") as file:
        file.writelines(text)


if __name__ == "__main__":
    main()
