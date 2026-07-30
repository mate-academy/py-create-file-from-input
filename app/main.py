def main() -> None:
    stop = False
    file_name = input("Enter name of the file: ") + ".txt"
    while not stop:
        with open(file_name, "w") as file:
            while not stop:
                content = input("Enter new line of content: ")
                if content.lower() == "stop":
                    stop = True
                else:
                    file.write((content + "\n"))


if __name__ == "__main__":
    main()
