def main() -> None:
    name = input("Enter name of the file: ")
    with (open(f"{name}.txt", "w") as n):
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            n.write(line + "\n")


if __name__ == "__main__":
    main()
