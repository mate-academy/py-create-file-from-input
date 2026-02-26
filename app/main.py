def main() -> None:
    filename = input("Enter name of the file: ")
    content = ""

    with open(f"{filename}.txt", "w") as f:
        while content != "stop":
            content = input("Enter new line of content: ")
            if content != "stop":
                f.write(content + "\n")


if __name__ == "__main__":
    main()
