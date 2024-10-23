def main() -> None:
    name = input("Enter name of the file: ")

    with open(name + ".txt", "w") as file:
        pass

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        with open(name + ".txt", "a") as file:
            file.write(line + "\n")


if __name__ == "__main__":
    main()