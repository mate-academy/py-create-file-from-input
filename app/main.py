def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "a") as f:
        while True:
            line = input("Enter new line of content: ")
            if str(line) == "stop":
                break
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
