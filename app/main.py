def main() -> None:
    name_file = input("Enter name of the file: ")
    with open(f"{name_file}.txt", "a") as my_file:
        info = input("Enter new line of content: ")
        while info != "stop":
            my_file.write(info + "\n")
            info = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
