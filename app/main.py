def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "a") as f:
        while True:
            content = input("Enter new line of content: ")

            if "stop" in content:
                break
            f.write(content + "\n")


if __name__ == "__main__":
    main()
