def main() -> None:
    name_file = input("Enter name of the file: ") + ".txt"
    with open(name_file, "a") as f:
        while True:
            pish = input("Enter new line of content: ")
            if pish.lower() == "stop":
                break

            f.write(pish + "\n")


if __name__ == "__main__":
    main()
