def main() -> None:
    filename = input("Enter name of the file: ")
    with open(f"{filename}.txt", "a", newline="") as f:
        while True:
            new_row = input("Enter new line of content: ")
            if new_row == "stop":
                break
            f.write(f"{new_row}\n")


if __name__ == "__main__":
    main()
