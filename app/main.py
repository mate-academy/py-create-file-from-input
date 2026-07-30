def main() -> None:
    name = input("Enter name of the file: ")
    while True:
        with open(f"./{name}.txt", "a") as file:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            file.write(f"{content}\n")


if __name__ == "__main__":
    main()
