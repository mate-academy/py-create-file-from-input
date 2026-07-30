def main() -> None:
    filename = input("Enter name of the file: ")

    with open(f"{filename}.txt", "w") as f:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            f.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
