def main() -> None:
    with open((input("Enter name of the file: ") + ".txt"), "a") as f:
        while True:
            new_text = (input("Enter new line of content: "))
            if new_text == "stop":
                break
            f.write(new_text + "\n")


if __name__ == "__main__":
    main()
