def main() -> None:
    file_name = str(input("Enter name of the file: ")) + ".txt"
    with open(file_name, "w") as file:
        while True:
            file_str = str(input("Enter new line of content: "))
            if file_str.lower() == "stop":
                break
            file.write(file_str + "\n")


if __name__ == "__main__":
    main()
