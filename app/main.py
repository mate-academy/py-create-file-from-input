def main() -> None:
    name = input("Enter name of the file: ")
    information = ""
    while True:
        something = input("Enter new line of content: ")
        if something == "stop":
            break
        information = information + something + "\n"

    with open(f"{name}.txt", "w") as file:
        file.write(information)


if __name__ == "__main__":
    main()
