def main() -> None:
    name = input("Enter name of the file: ")

    with open(f"{name}.txt", "w") as f:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            f.write(text + "\n")

if __name__ == "__main__":
    main()
