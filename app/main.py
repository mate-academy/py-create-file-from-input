def main() -> None:
    filename = input("Enter name of the file: ")
    with open(f"{filename}.txt", "w") as f:
        while True:
            line_text = input("Enter new line of content: ")
            if line_text == "stop":
                break
            f.write(f"{line_text}\n")


if __name__ == "__main__":
    main()
