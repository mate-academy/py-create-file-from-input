def main() -> None:
    file_name = str(input("Enter name of the file: ")) + ".txt"
    with open(file_name, "w") as f:
        while True:
            some_text = input("Enter new line of content: ")
            if some_text == "stop":
                break
            f.write(some_text + "\n")


if __name__ == "__main__":
    main()
