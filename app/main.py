def main() -> None:
    name_of_file = input("Enter name of the file: ")
    with open(f"{name_of_file}.txt", "w") as f:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            else:
                f.write(f"{text}\n")


if __name__ == "__main__":
    main()
