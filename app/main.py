def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "a") as name:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            name.write(f"{content}\n")


if __name__ == "__main__":
    main()
