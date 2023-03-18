def main() -> None:
    name = input("Enter name of the file: ")
    while True:
        message = input("Enter new line of content: ")
        with open(f"{name}.txt", "a") as f:
            if message != "stop":
                f.write(f"{message}\n")
            else:
                break


if __name__ == "__main__":
    main()
