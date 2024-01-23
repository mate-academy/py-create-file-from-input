def main() -> None:
    file_name = f"{input('Enter name of the file: ')}.txt"
    with open(file_name, "a") as file:
        while True:
            line = input("Enter new line of content: ")
            if line.lower() == "stop":
                break
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
