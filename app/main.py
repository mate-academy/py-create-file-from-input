def main() -> None:

    name = input("Enter name of the file: ")

    is_stop = True
    with open(name + ".txt", "w") as file:
        while is_stop:
            content = input("Enter new line of content: ")
            if content == "stop":
                is_stop = False
            else:
                file.write(content + "\n")


if __name__ == "__main__":
    main()
