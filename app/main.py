def main() -> None:
    name = input("Enter name of the file: ")

    with open(name + ".txt", "a") as f:
        while True:
            line = input("Enter new line of content: ")

            if line.lower() == "stop":
                break
            else:
                f.write(f"{line}\n")


if __name__ == "__main__":
    main()
