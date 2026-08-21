def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w") as w:
        content = input("Enter new line of content: ")
        while content != "stop":
            w.write(content + "\n")
            content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
