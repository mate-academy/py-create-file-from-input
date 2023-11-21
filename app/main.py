def main() -> None:
    name = input("Enter name of the file: ")
    text = ""
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            text += line + "\n"
    with open(f"{name}.txt", "w") as file:
        file.write(text)


if __name__ == "__main__":
    main()
