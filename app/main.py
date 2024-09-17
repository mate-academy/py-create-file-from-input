def main() -> None:
    file_name = str(input("Enter name of the file: "))

    with open(f"{file_name}.txt", "w+") as file:
        while True:
            line = str(input("Enter new line of content: "))
            if line == "stop":
                break
            file.write(line + "\n")
        file.seek(0)
        print(file.read())


if __name__ == "__main__":
    main()
