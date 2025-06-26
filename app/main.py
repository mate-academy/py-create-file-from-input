def main() -> None:
    name = input("Enter name of the file: ")
    try:
        while True:
            with open(f"{name}.txt", "a") as file:
                content = input("Enter new line of content: ")
                if content != "stop":
                    file.write(f"{content}\n")
                if content == "stop":
                    break
    except ValueError:
        raise ValueError


if __name__ == "__main__":
    main()
