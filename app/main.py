def main() -> object:
    with open(input("Enter name of the file: ") + ".txt", "a") as my_file:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            my_file.write(f"{text}\n")


if __name__ == "__main__":
    main()
