def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "x") as output_file:
        while True:
            word = input("Enter new line of content: ")

            if word == "stop":
                break
            else:
                output_file.write(f"{word}\n")


if __name__ == "__main__":
    main()
