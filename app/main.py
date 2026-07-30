def main() -> None:
    name = input("Enter name of the file: ")
    text = input("Enter new line of content: ")
    with open(f"{name}.txt", "a") as f:
        while text != "stop":
            f.write(f"{text}\n")
            text = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
