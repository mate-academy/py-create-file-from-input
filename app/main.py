def main() -> None:
    name = input("Enter name of the file: ")
    created_file = open(f"{name}.txt", "w")
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        created_file.write(line + "\n")


if __name__ == "__main__":
    main()
