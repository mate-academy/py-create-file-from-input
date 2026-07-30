def main() -> None:
    name = input("Enter name of the file: ")
    open(f"{name}.txt", "a")

    line = ""
    while line.lower() != "stop":
        with open(f"{name}.txt", "a") as f:
            line = input("Enter new line of content: ")

            if line.lower() != "stop":
                f.write(f"{line}\n")


if __name__ == "__main__":
    main()
