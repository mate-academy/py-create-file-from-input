def main() -> str:
    name = input("Enter name of the file: ")
    file_name = open(f"{name}.txt", "a+")
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        file_name.write(line + "\n")


if __name__ == "__main__":
    main()
