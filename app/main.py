def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as file:
        while True:
            line = input("Enter new line of content: ")
            if line != "stop":
                file.write(f"{line}\n")
            else:
                break


if __name__ == "__main__":
    main()
