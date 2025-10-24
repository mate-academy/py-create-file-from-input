def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(file_name + ".txt", "a") as f:
        while True:
            text = input("Enter new line of content: ")
            if text.lower() == "stop":
                break
            f.write(text + "\n")


if __name__ == "__main__":
    main()
    # refactored 2.20.24
    
