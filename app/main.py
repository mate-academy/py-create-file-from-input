def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as s:
        while True:
            new = input("Enter new line of content: ")
            if new == "stop":
                break
            s.write(new + "\n")


if __name__ == "__main__":
    main()
