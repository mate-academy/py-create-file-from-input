def main() -> None:

    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "w") as f:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
