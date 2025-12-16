def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as f:
        while (line := input("Enter new line of content: ")) != "stop":
            f.write(line + "\n")


if __name__ == "__main__":
    main()
