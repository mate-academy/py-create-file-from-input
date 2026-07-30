def main() -> None:
    name = str(input("Enter name of the file: "))
    with open(f"{name}.txt", "w") as f:
        while True:
            line = str(input("Enter new line of content: "))
            if line == "stop":
                break
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
