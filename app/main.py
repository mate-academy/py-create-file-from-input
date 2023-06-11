def main() -> None:
    name = input("Enter name of the file: ")
    with open(name + ".txt", "w") as f:
        content = input("Enter new line of content: ")
        while content != "stop":
            f.write(content + "\n")
            content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
