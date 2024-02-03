def main() -> None:
    name = input("Enter name of the file: ")
    with open(name + ".txt", "a") as f:
        while True:
            new_content = input("Enter new line of content: ")
            if new_content == "stop":
                break
            f.write(new_content + "\n")


if __name__ == "__main__":
    main()
