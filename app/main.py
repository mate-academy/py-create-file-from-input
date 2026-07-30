def main() -> None:

    file_name = input("Enter name of the file: ")
    if file_name:
        with open(f"{file_name}.txt", "a") as f:
            while True:
                line = input("Enter new line of content: ")
                if line.lower() == "stop":
                    break
                f.write(f"{line}\n")


if __name__ == "__main__":
    main()
