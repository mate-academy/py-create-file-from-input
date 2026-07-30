def main() -> None:
    filename = input("Enter name of the file: ")
    text = ""
    with open(f"{filename}.txt", "w") as f:
        while text != "stop":
            text = input("Enter new line of content: ")
            if text != "stop":
                f.write(f"{text}\n")


if __name__ == "__main__":
    main()
