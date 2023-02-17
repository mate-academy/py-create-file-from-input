def main() -> None:
    name = input("Enter name of the file: ")
    with open(name + ".txt", "w") as file:
        while True:
            enter = input("Enter new line of content: ")
            if enter != "stop":
                file.write(f"{enter}\n")
            else:
                break


if __name__ == "__main__":
    main()
