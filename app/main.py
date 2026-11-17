def main() -> None:
    # write your code here
    name = input("Enter name of the file: ")
    while True:
        content = input("Enter new line of content: ")
        with open(f"{name}.txt", "a") as f:
            if content == "stop":
                break
            f.write(content + "\n")


if __name__ == "__main__":
    main()
