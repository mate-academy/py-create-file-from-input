def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    text = ""
    while True:
        temp = input("Enter new line of content: ")
        if temp.lower() == "stop":
            break
        text += temp + "\n"

    with open(name, "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
