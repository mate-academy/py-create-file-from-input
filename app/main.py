def main() -> None:
    new_name = input("Enter name of the file: ")
    with open(f"{new_name}.txt", "w") as a:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            a.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
