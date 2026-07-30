def main() -> None:
    file_name = input("Enter name of the file: ")
    full_name = file_name + ".txt"
    while True:
        with open(full_name, "a") as f:
            message = input("Enter new line of content: ")
            if message == "stop":
                break
            f.write(message + "\n")


if __name__ == "__main__":
    main()
