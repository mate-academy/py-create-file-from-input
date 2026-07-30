def main() -> None:
    name = input("Enter name of the file: ")
    content = ""

    while True:
        inp = input("Enter new line of content: ")
        if inp == "stop":
            break

        content += inp + "\n"

    with open(name + ".txt", "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
