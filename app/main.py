def main() -> None:
    name1 = input("Enter name of the file: ")
    with open(f"{name1}.txt", "w", newline="\n") as f:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            else:
                f.write(f"{line}\n")


if __name__ == "__main__":
    main()
