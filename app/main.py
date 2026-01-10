def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w") as f:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            f.write(line + "\n")


if __name__ == "__main__":
    main()
