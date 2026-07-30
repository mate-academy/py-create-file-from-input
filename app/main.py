def main() -> None:
    filename = input("Enter name of the file: ")
    with open(f"{filename}.txt", "w") as f:
        while True:
            line = input("Enter new line of content: ")
            if line.strip().lower() == "stop":
                break
            f.write(line + "\n")


if __name__ == "__main__":
    main()
