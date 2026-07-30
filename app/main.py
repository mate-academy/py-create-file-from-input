def main() -> None:
    name_of_file = input("Enter name of the file: ")
    with open(f"{name_of_file}.txt", "a") as f:
        while True:
            string = input("Enter new line of content: ")
            if string == "stop":
                break
            f.write(f"{string}\n")


if __name__ == "__main__":
    main()
