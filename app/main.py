def main() -> None:
    name = input("Enter name of the file: ") + ".txt"

    with open(f"{name}", "w") as f:
        pass

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        with open(f"{name}", "a") as f:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
