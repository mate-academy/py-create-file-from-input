def main() -> None:
    file_name = input("Enter name of the file: ")
    full_file_name = file_name + ".txt"
    with open(full_file_name, "w") as file:
        while True:
            words = input("Enter new line of content: ")
            if words == "stop":
                break
            file.write(words + "\n")


if __name__ == "__main__":
    main()
