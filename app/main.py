def main() -> None:

    file_name = input("Enter name of the file: ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    res = ""

    while True:
        inp = input("Enter new line of content: ")
        if inp == "stop":
            break
        res += inp + "\n"

    with open(file_name, "w") as file:
        file.write(res)


if __name__ == "__main__":
    main()
