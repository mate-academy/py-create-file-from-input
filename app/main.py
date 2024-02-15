def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as file_name:
        while True:
            word = input("Enter new line of content: ")
            if word == "stop":
                break
            file_name.write(word + "\n")


if __name__ == "__main__":
    main()
