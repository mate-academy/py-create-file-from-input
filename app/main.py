def main() -> None:
    filename = input("Enter name of the file: ")
    with open(f"{filename}.txt", 'a') as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            f.write(content + "\n")


if __name__ == "__main__":
    main()



