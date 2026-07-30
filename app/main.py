def main() -> None:
    name1 = f'{input("Enter name of the file: ")}.txt'
    new_file = open(name1, "w")

    while True:
        new_string = f"{input('Enter new line of content: ')}"
        if new_string == "stop":
            break
        else:
            new_file.write(f"{new_string}\n")
    new_file.close()


if __name__ == "__main__":
    main()
