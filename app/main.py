def main() -> None:
    filename = input("Enter name of the file: ")
    with open(f"{filename}.txt", "w") as f:
        while (line := input("Enter new line of content: ")) != "stop":
            f.write(line + "\n")


if __name__ == "__main__":
    main()
