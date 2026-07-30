def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    with open(name, "w") as f:
        while True:
            enter = input("Enter new line of content: ")
            if enter == "stop":
                break
            f.write(enter + "\n")


if __name__ == "__main__":
    main()
