def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    with open(name, mode="a") as f:

        while True:
            content = input("Enter new line of content: ")
            print(content)
            if content == "stop":
                break
            f.write(content + "\n")


if __name__ == "__main__":
    main()
