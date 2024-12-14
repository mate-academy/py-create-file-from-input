def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, "w") as fl:
        while True:
            value = input("Enter new line of content: ")
            if value == "stop":
                break
            fl.write(f"{value}\n")


if __name__ == "__main__":
    main()
