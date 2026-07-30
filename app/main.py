def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    open(file_name, "a").close()
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        with open(file_name, "a") as file:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
