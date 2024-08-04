def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "a") as new_file:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            else:
                new_file.write(f"{text}\n")


if __name__ == "__main__":
    main()
