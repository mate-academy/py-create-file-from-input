def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    with open(filename, "a") as f:
        while True:
            new_string = input("Enter new line of content: ")
            if new_string != "stop":
                f.write(new_string + "\n")
            else:
                break


if __name__ == "__main__":
    main()
