def main() -> None:
    name = str(input("Enter name of the file: "))
    with open(f"{name}.txt", "w") as file:
        cont = True
        while cont:
            text = str(input("Enter new line of content: "))
            if text == "stop":
                break
            file.write(f"{text}\n")


if __name__ == "__main__":
    main()
