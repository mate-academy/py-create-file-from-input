def main() -> None:
    name = input("Enter name of the file: ")
    with open(name + ".txt", "a") as file:
        while True:
            input_ = input("Enter new line of content: ")
            if input_ == "stop":
                break
            file.write(input_ + "\n")


if __name__ == "__main__":
    main()
