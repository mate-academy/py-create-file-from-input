def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, "w") as f:
        while True:
            name = input("Enter new line of content: ")
            if name == "stop":
                break
            f.write(name + "\n")


if __name__ == "__main__":
    main()
