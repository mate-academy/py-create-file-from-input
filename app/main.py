def main() -> None:
    name = input("Enter name of the file: ")
    while True:
        line = input("Enter new line of content: ")
        my_file = open(name + ".txt", "a")
        if line == "stop":
            break
        my_file.write(f"{line}\n")
        my_file.close()


if __name__ == "__main__":
    main()
