def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = file_name + ".txt"
    with open(file_name, "a") as f:
        while True:
            ask = input("Enter new line of content: ")
            if ask == "stop":
                break
            f.write(ask + "\n")


if __name__ == "__main__":
    main()
