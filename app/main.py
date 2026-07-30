def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file:
        while True:
            line = input("Enter new line of content: ")
            if line != "stop":
                file.write(line + "\n")
            else:
                break


if __name__ == "__main__":
    main()
