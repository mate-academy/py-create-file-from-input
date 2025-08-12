def main() -> None:
    name = input("Enter name of the file: ")
    txt = ""

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        txt += f"{line}\n"

    with open(f"{name}.txt", "a") as file:
        file.write(txt)


if __name__ == "__main__":
    main()
